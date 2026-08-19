import logging
import re
import os
import json
import time

import requests
from urllib import parse,error
import multiprocessing


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s -%(lineno)d",
)

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0'
}

base_url = 'https://lzacg.cc'
total_page_num = 66


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


def parse_list_url(page_url):
    """对列表页请求并进行分析,返回html数据"""
    try:
        res = requests.get(page_url,headers=headers)
    except error.HTTPError as e:
        if res.status_code == requests.codes.not_found:
            logging.info('所有页面已全部采集完毕')
            return None
        logging.error(f'请求失败：{e.reason}')
    else:
        logging.info(f'网站解析成功')
        return res.text


def parse_list_html(html):
    """
        返回的是这个列表网站的所有galgame数据，大概16个
        :return galgamelist
    """
    try:
        url_picture_name = re.compile(r'<posts.*?<a.*?target="_blank".*?href="(.*?)">.*?<img.*?data-src="(.*?)"\salt="(.*?)".*?>', re.S)
        results = re.finditer(url_picture_name,html)
    except Exception as e:
        logging.error(f'正则匹配失败{e}')
    else:
        list_game = []
        for result in results:
            url,picture,name = result.group(1),result.group(2),result.group(3)
            list_game.append({
                'url':url,
                'picture':picture,
                'name':name.rstrip('-量子ACG')
            })
        logging.info('数据生成成功.....（待保存到文件中）')
        yield list_game


def save_url_data(list_game,page):
    """
    将每一个以业为单位，将每一页的galgame以json格式保存，每一页对应一个json文件
    :param list_game: galgame数据
    :param page: 页数
    :return: 游戏的名字和url详细地址
    """
    os.chdir('..\\资料文件')
    None if os.path.exists('量子acg平台数据(上)') else os.makedirs('量子acg平台数据(上)')

    try:
        json.dump(list_game,open(f'量子acg平台数据(上)\\page{page}.json','w',encoding='utf-8'),ensure_ascii=False,indent=4)
    except Exception as e:
        logging.error('文件保存失败')
        return None
    else:
        logging.info('文件(上部)保存成功')


# def parse_detail_url(detail_url):
#     """
#     :param detail_url: galgame详细页面
#     :return: 详细页面的html
#     """
#     try:
#         res = requests.get(detail_url,headers=headers)
#     except error.HTTPError as e:
#         logging.error(f'请求失败：{e.reason}')
#     else:
#         logging.info(f'galgame游戏解析成功')
#         return res.text


# 此处应使用xpath来进行数据的提取
# def parse_detail_html(html):
#     pass



# def main1(page):
#     page_url = list_url(page)
#     page_html = parse_list_url(page_url)
#     if page_html == None:
#         return False
#     game_list = list(parse_list_html(page_html))
#     save_url_data(game_list,page)
#     return True



if __name__ == "__main__":
    for page in range(1,total_page_num+1):
        page_url = list_url(page)
        page_html = parse_list_url(page_url)
        game_list = list(parse_list_html(page_html))
        save_url_data(game_list,page)






