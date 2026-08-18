import logging
import re
import os
import json
import time

import requests
from urllib import parse
import multiprocessing


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s -%(lineno)d",
)
base_url = 'https://ssr1.scrape.center'
total_page = 10
logging.info('程序正常运行')


def scrape_index(page):
    """
    列表页查找
    :params 传入页码
    :return 返回拼接好的url
    """
    index_url = f'{base_url}/page/{page}'
    return index_url


def scrape_page(url):
    """
    列表页爬取
    :param url: 传入一个url链接
    :return: 返回网点的html文件
    """
    logging.info(f'开始爬取链接：{url}的数据')
    try:
        res = requests.get(url)
        if res.status_code == requests.codes.ok:
            return res.text
        else:
            logging.error(f'get invalid status_code: {res.status_code} while scrape url:{res.url}')
    except requests.RequestException as e:
        logging.error(f'error occurred while scrape ulr:{url}page')


def parse_index(html):
    """
    列表页的解析
    :param html: 列表页的html
    :return: 解析后的地址
    """
    pattern = re.compile(r'<a\s.*?href="(.*?)"\sclass="name">')
    items = re.finditer(pattern, html)
    for item in items:
        # item 现在是Match对象，可以使用 .group(1)
        detail_url = parse.urljoin(base_url, item.group(1))
        yield detail_url



def scrape_detail(url):
    """返回详细页面的html数据"""
    detail_html = scrape_page(url)
    return detail_html


def parse_detail(html):
    """对详细页的解析与处理"""
    conver = re.compile(r'class="item.*?<img.*?src="(.*?)"\s+class="cover">',re.S)
    name = re.compile(r'<h2.*?>(.*?)</h2>')
    categories = re.compile(r'<button.*?category.*?<span>(.*?)</span>',re.S)
    published_at = re.compile(r'\d{4}-\d{2}-\d{2}\s上映',re.S)
    drama = re.compile(r'<h3.*?>剧情简介</h3>.*?<p.*?>\s*(.*?)\s*</p>',re.S)
    score = re.compile(r'class="score.*?>\s*(.*?)</p>',re.S)

    conver_parm = re.search(conver,html).group(1) if re.search(conver,html) else None
    name_parm = re.search(name,html).group(1) if re.search(name,html) else None
    categories_parm = re.findall(categories,html) if re.findall(categories,html) else None
    published_at_parm = re.search(published_at,html).group() if re.search(published_at,html) else None
    drama_parm = re.search(drama,html).group(1) if re.search(drama,html) else None
    score_parm = re.search(score,html).group(1) if re.search(score,html) else None

    movie_field_data = {
        '封面图片地址':conver_parm,
        '电影名字':name_parm,
        '类型':categories_parm,
        '简介':drama_parm,
        '上映时间':published_at_parm,
        '豆瓣评分':score_parm
    }
    logging.info(f'电影{name_parm}数据采集成功........待保存到文本')
    return movie_field_data


def save_data(dict_data,lock):
    try:
        os.chdir('..\\资料文件')
        filename = 'movie_data文件'
        None if os.path.exists(filename) else os.makedirs(filename)
    except Exception as e:
        logging.error('创建文件失败')
        return None

    movie_name = dict_data.get('电影名字')
    movie_data = {'电影名字':movie_name,'详细数据':dict_data}

    lock.acquire()
    try:
        with open(f'{filename}\\{movie_name}.json','w',encoding='utf-8') as f:
            json.dump(movie_data,f,ensure_ascii=False,indent=4)
            f.write('\n')
            logging.info(f'电影：{movie_name}数据已保存到文本')
    finally:
        lock.release()
def main1():
    for page in range(1,total_page+1):
        page_url = scrape_index(page)
        page_html = scrape_page(page_url)
        movies_url = parse_index(page_html)  # 电影详情页的url生成器
        for movie_url in movies_url:
            movie_html = scrape_detail(movie_url)
            movie_data = parse_detail(movie_html) #字典数据
            save_data(movie_data,multiprocessing.Lock())

def main2(page):
    index_html_url = scrape_index(page)
    index_html = scrape_page(index_html_url)
    details_url = parse_index(index_html) # 电影详情页的url生成器
    for detail_url in details_url:
        detail_html = scrape_detail(detail_url)
        detail_data = parse_detail(detail_html)
        save_data(detail_data,multiprocessing.Lock())


if __name__ == '__main__':
    start_time = time.perf_counter()
    main1()
    end_time = time.perf_counter()
    cost = end_time - start_time
    print(f"程序运行耗时：{cost:.2f} 秒") # 用时78.24秒


    # start_time = time.perf_counter()
    # process_list = []
    # for i in range(1,total_page+1):
    #     result = multiprocessing.Process(target=main2,args=(i,))
    #     process_list.append(result)
    # for i in process_list:
    #     i.start()
    # for p in process_list:
    #     p.join()
    # end_time = time.perf_counter()
    # cost = end_time - start_time
    # print(f"程序运行耗时：{cost:.2f} 秒") # 用时19.25秒

    print('完成')

