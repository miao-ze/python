from lxml import etree
import requests



def save_file(file,data):
    with open(file,'w',encoding='utf-8') as f:
        f.write(data)

url_bi = 'https://www.bilibili.com/'
url_lz = 'https://lzacg.cc/'
url_bu = 'https://www.baidu.com'
url_mv = 'https://ssr1.scrape.center/'
url_hp_p = 'https://www.httpbin.org/post'
url_hp_g = 'https://www.httpbin.org/get'



res = requests.get(url_lz)
save_file('..\\资料文件\\lzacg.html',res.text)



































































