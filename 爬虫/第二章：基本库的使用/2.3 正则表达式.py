import re
import requests



url_bi = 'https://www.bilibili.com/'
url_lz = 'https://lzacg.cc/'
url_bu = 'https://www.baidu.com'
url_mv = 'https://ssr1.scrape.center/'
url_hp_p = 'https://www.httpbin.org/post'
url_hp_g = 'https://www.httpbin.org/get'


import re
res = requests.get(url_lz)
# 改用 re.search，加上非贪婪模式 .*?，开启单行模式 DOTALL
result = re.search(r'<img.*?>', res.text, re.S)
if result:
    print(result.group())
else:
    print("没有找到图片标签")

    v bnkmkjn