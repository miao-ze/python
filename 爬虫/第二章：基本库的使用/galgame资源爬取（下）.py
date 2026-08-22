import logging
import os
import json
import time

import requests
from urllib import parse,error
from multiprocessing import Pool
from bs4 import BeautifulSoup
from lxml import etree


base_url = 'https://lzacg.cc'

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s -%(lineno)d",
)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0'
}

# 1
def list_url(page):
    """找到所有的列表页面"""
    try:
        page_url = parse.urljoin(base_url,f'/category/galgame/page/{page}')
    except Exception as e:
        logging.error('列表页url拼接失败')
        return None
    else:
        logging.info(f'即将爬取网页：{page_url}')
        return page_url


# 2
def parse_list_url(page_url):
    """对列表页请求并进行分析,返回html列表页的结果数据"""
    try:
        res = requests.get(page_url,headers=headers)
    except error.HTTPError as e:
        logging.error(f'请求失败：{e.reason}')
    else:
        logging.info(f'网页请求成功...(后采集)')
        return res.text


# 3
def parse_list_html(html):
    """
        返回的是这个列表网站的所有galgame数据，大概16个
        :return 每个gal游戏的名字、图片、链接地址
    """
    try:
        soup = BeautifulSoup(html,'lxml')
        urls = soup.select('.posts-item.ajax-item.card .item-thumbnail a')
    except Exception as e:
        logging.error('网页数据提取失败')
    else:
        page_galgame_url = [url['href'] for url in urls]
        logging.info('该网页数据解析完成.....（即将对每个游戏进行请求）')
        return page_galgame_url



# 4
def parse_detail_galgame_wed(url):
    """
    对每一个gal游戏页面进行请求
    :param url 游戏地址
    :return: gal的html源码
    """
    game_html = parse_list_url(url)
    return game_html


# 5
def parse_detail_galgame_data(html):
    """
    对gal游戏网站的html进行解析
    :param html:
    :return: 游戏描述信息和名字
    """
    xp = '''
        (//div[contains(@class,"wp-posts-content")]/h4[@class="wp-block-heading"])[1]
        /following-sibling::p[count(preceding-sibling::h4[@class="wp-block-heading"])=1]/text()
         '''

    data = etree.HTML(html)

    describe_galgame = '\n'.join(data.xpath(xp))

    name = data.xpath('//title/text()')
    name_galgame = name[0].rstrip('-量子ACG')

    url_galgame = data.xpath('//link[@rel="canonical"]/@href')[0]
    try:
        img_galgame = data.find(".//figure/img").get('src')
    except Exception as e:
        print('图片地址解析错误')
        return None

    logging.info('完成...')
    return {"游戏名称":name_galgame,"地址":url_galgame,"描述":describe_galgame,'图片':img_galgame}


# 6
def save_document(data,page):
    """
    保存文件
    :param data:
    :return:
    """
    os.chdir('..\\资料文件')
    None if os.path.exists('量子acg平台数据(下)') else os.makedirs('量子acg平台数据(下)')

    try:
        json.dump(data,open(f'量子acg平台数据(下)\\page{page}页.json','w',encoding='utf-8'),ensure_ascii=False,indent=4)
    except Exception as e:
        logging.error('文件保存失败')
        return None
    else:
        logging.info('文件保存成功')


def main(page):
    page_url = list_url(page)
    page_html = parse_list_url(page_url)
    page_list = []
    for game_url in parse_list_html(page_html):   # 这是一个生成器：返回所有游戏的主页连接，列表，元素是url地址
        # 通过url来查找游戏的html源码
        game_html = parse_detail_galgame_wed(game_url)
        # 对源码进行解析，得到name、url和describe
        galgame_data = parse_detail_galgame_data(game_html)
        page_list.append(galgame_data)
    # 进行保存
    save_document(page_list,page)




if __name__ == "__main__":

    start_time = time.time()

    total_page_num = 65

    pool = Pool(processes=10)
    result_obj = pool.map_async(main,range(1,total_page_num+1))

    try:
        # 设置总超时120秒，超过直接报错，不会无限挂住
        all_result = result_obj.get(timeout=60)
    except Exception as e:
        print(f"等待任务超时/异常：{e}，完成采集用时：{time.time() - start_time}")
    pool.close()
    pool.join()

    print(f'完成采集用时：{time.time() - start_time}')







