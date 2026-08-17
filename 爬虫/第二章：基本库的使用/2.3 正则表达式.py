import re
import requests



url_bi = 'https://www.bilibili.com/'
url_lz = 'https://lzacg.cc/'
url_bu = 'https://www.baidu.com'
url_mv = 'https://ssr1.scrape.center/'
url_hp_p = 'https://www.httpbin.org/post'
url_hp_g = 'https://www.httpbin.org/get'


def save_file(file,data):
    with open(file,'w',encoding='utf-8') as f:
        f.write(data)

# res = requests.get(url_lz)
# save_file('..\\资料文件\\lzacg.html',res.text)
# result = re.search('<title>.*?</title>.*?>',res.text,re.S)
# print(result.group())


# res = requests.get(url_lz)
# data = res.text
# results = re.findall(r'<a sid=.*?>.*?</a>',data,re.S)
# for result in results:
#     print(result)


# with open('../资料文件/lzacg.html', 'r', encoding='utf-8') as f:
#     data = f.read()
#     result = re.sub(r'\S+',' ',data,re.S)
#     print(result)