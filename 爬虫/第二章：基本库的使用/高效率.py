import logging
import re
import json
import time  # <--- 修复：补上缺失的导入
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin

import requests
from lxml import etree

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s - %(lineno)d",
)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0'
}

BASE_URL = 'https://lzacg.cc'
TOTAL_PAGE_NUM = 4
MAX_WORKERS = 10          # 并发线程数
RETRY_TIMES = 3           # 请求失败重试次数

# 数据保存目录
SAVE_DIR = Path(__file__).parent / '资料文件' / '量子acg平台数据(下)'
SAVE_DIR.mkdir(parents=True, exist_ok=True)


def list_url(page):
    """生成列表页 URL"""
    return urljoin(BASE_URL, f'/category/galgame/page/{page}')


def fetch_html(url, session=None, retry=RETRY_TIMES):
    """
    带重试的请求函数，返回 HTML 文本或 None
    """
    if session is None:
        session = requests.Session()
    for attempt in range(retry):
        try:
            resp = session.get(url, headers=HEADERS, timeout=10)
            resp.raise_for_status()
            return resp.text
        except Exception as e:
            logging.warning(f"请求 {url} 失败 (尝试 {attempt+1}/{retry}): {e}")
            time.sleep(1)  # 简单退避
    logging.error(f"请求 {url} 重试 {retry} 次后仍失败")
    return None


def parse_list_html(html):
    """
    解析列表页，返回所有游戏详情页 URL 列表
    优先使用 lxml XPath，失败时回退到正则
    """
    try:
        tree = etree.HTML(html)
        # 查找所有文章链接
        urls = tree.xpath('//article[contains(@class,"post")]//a[contains(@href,"/archives/")]/@href')
        urls = list(dict.fromkeys(urls))
        if urls:
            return urls
    except Exception:
        pass

    # 回退正则（修复：加上 re.S 让 . 匹配换行）
    pattern = re.compile(r'<a.*?target="_blank".*?href="(.*?)"', re.S)
    urls = pattern.findall(html)
    # 过滤掉非游戏链接
    urls = [u for u in urls if '/archives/' in u]
    return urls


def fetch_game_data(game_url):
    """
    请求并解析单个游戏详情页，返回字典 {name, url, describe}
    若失败返回 None
    """
    html = fetch_html(game_url)
    if not html:
        return None

    try:
        tree = etree.HTML(html)
        # 标题
        title = tree.xpath('//title/text()')
        name = title[0].rstrip('-量子ACG') if title else "未知名称"

        # 描述
        desc_nodes = tree.xpath(
            '(//div[contains(@class,"wp-posts-content")]/h4[@class="wp-block-heading"])[1]/following-sibling::p[1]/text()'
        )
        describe = '\n'.join(desc_nodes).strip() if desc_nodes else "无描述"

        # 规范 URL
        canon = tree.xpath('//link[@rel="canonical"]/@href')
        url = canon[0] if canon else game_url

        logging.info(f"解析成功: {name}")
        return {"name": name, "地址": url, "describe": describe}
    except Exception as e:
        logging.error(f"解析 {game_url} 时出错: {e}")
        return None


def save_page_data(page_data, page_num):
    """保存单页数据为 JSON"""
    save_path = SAVE_DIR / f'page{page_num}页.json'
    try:
        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(page_data, f, ensure_ascii=False, indent=4)
        logging.info(f"第 {page_num} 页数据已保存至 {save_path}")
    except Exception as e:
        logging.error(f"保存第 {page_num} 页失败: {e}")


def process_page(page_num):
    """处理一个列表页：获取所有游戏链接，并发爬取详情，返回数据列表"""
    page_url = list_url(page_num)
    logging.info(f"开始处理第 {page_num} 页: {page_url}")

    # 1. 获取列表页 HTML
    html = fetch_html(page_url)
    if not html:
        logging.error(f"第 {page_num} 页列表请求失败")
        return []

    # 2. 解析出所有游戏链接
    game_urls = parse_list_html(html)
    if not game_urls:
        logging.warning(f"第 {page_num} 页未解析到任何游戏链接")
        return []

    logging.info(f"第 {page_num} 页发现 {len(game_urls)} 个游戏")

    # 3. 使用线程池并发请求每个游戏详情
    games_data = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_url = {executor.submit(fetch_game_data, url): url for url in game_urls}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                result = future.result()
                if result:
                    games_data.append(result)
            except Exception as e:
                logging.error(f"处理 {url} 时发生异常: {e}")

    logging.info(f"第 {page_num} 页成功获取 {len(games_data)} 个游戏数据")
    return games_data


def main():
    for page_num in range(1, TOTAL_PAGE_NUM + 1):
        page_data = process_page(page_num)
        if page_data:
            save_page_data(page_data, page_num)
        time.sleep(0.5)  # 适当延时


if __name__ == "__main__":
    main()