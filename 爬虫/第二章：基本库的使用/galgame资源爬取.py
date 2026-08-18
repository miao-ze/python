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


base_url = 'https://www.nekogal.com'
total_page_num = 10


def list_url(page):
    """找到所有的列表页面"""
    try:
        page_url = parse.urljoin(base_url,f'/page/{page}')
    except Exception as e:
        logging.error('列表页url拼接失败')
        return None
    else:
        return page_url


def parse_list_url(page_url):
    """对列表页进行分析"""
    res = requests.get(page_url)

