import socket
from http.cookiejar import CookieJar
from http import cookiejar
from urllib import request,parse,error,robotparser
from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener, urlopen,ProxyHandler
from urllib.request import HTTPCookieProcessor
from urllib import error
from urllib import robotparser
import urllib3
from requests import Request

url1_bi = 'https://www.bilibili.com/'
url2_lz = 'https://lzacg.cc/'
url3_bu = 'https://www.baidu.com'
url4_mv = 'https://ssr1.scrape.center/'
url_hp_p = 'https://www.httpbin.org/post'
url_hp_g = 'https://www.httpbin.org/get'

def save_file(file,data):
    with open(file,'w',encoding='utf-8') as f:
        f.write(data)

# res = requests.get(url3_bu)
# print(res.status_code)
# print(type(res.text))
# print(res.cookies)
# print(res.content)


# res2 = requests.get('https://www.httpbin.org/get',params={'name':'阿斯顿','age':32})
# print(res2.json())
# print(res2.text)


# res = requests.get(url4_mv)
# pattern = re.compile('<h2.*?>(.*?)</h2.*?>',re.S)
# titles = re.findall(pattern,res.text)
# print(titles)


# res2 = requests.get(url4_mv)
# print(res2.text)
# print()
# print(res2.content)


# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0'
# }
# res = requests.get(url1_bi,headers=headers)
# print(res.text)
# save_file('资料文件\\2.html',res.text)
# data = request.Request(url=url1_bi,headers=headers,method='GET')
# res = request.urlopen(data)
# print(res.read().decode('utf-8'))


# data = {'name':'苗泽','age':21}
# res = requests.get(url4_mv,data=data)
# print(res.status_code)
# print(res.headers)
# print(res.cookies)
# print(res.history)
# print(res.url)
# print('成功') if res.status_code == requests.codes.ok else print('失败')


# file = {'file':open('资料文件\\1.webp','rb')}
# res = requests.post(url_hp_p,files=file)
# print(res.text)



import urllib3
import logging

# urllib3.disable_warnings()
# logging.captureWarnings(True)
# cookies = ('_octo=GH1.1.1469904663.1775034346; _device_id=143e6d44802f266f842446fe6d997704;'
#            ' saved_user_sessions=226444004%3A2-QYKMceZ2fy8ItgcqeLutVPj8beo3mSQsZx8sJ3r3qZ4o-s;'
#            ' user_session=2-QYKMceZ2fy8ItgcqeLutVPj8beo3mSQsZx8sJ3r3qZ4o-s; __Host-user_session_same_site=2-QYKMceZ2fy8ItgcqeLutVPj8beo3mSQsZx8sJ3r3qZ4o-s; logged_in=yes; '
#            'dotcom_user=miao-ze; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; '
#            'cpu_bucket=xlg; preferred_color_mode=light; tz=Asia%2FShanghai; _gh_sess=xsq3wlwQF9ZzBMoHeLLWhdvo8j9yPcGXWmEvaHP11JbenC%2FuQlkrIyUuu9IcTWEbNFb9A88%2FYvHGrG7cqlnSj8ymowNAib6OGhS%2F3AmqBh%2B4t83b09PszsC6dA%2BM7Y1EtOog0vLoQ8cZiizks4stSeGORulrA%2F'
#            'nnHkEiAGquUb2ppdGl4kuhBzw94j%2FauxZph5ltbQWLb7UZaEWhNgyQNVZBC9NFjrmNUg%2F3p%2BZ3I331PG1%2FCHuds2SXTaK%2FxJecuJc9NYkB6XGPW2cRupL%2FPGZJPSblrT9rLKGwxvqedffdOKRVKNo5RpU08evzVTpxf1kwrIV4XdsorMV0utOKuAB8BPZAcY2nyv9ZAIC6oPxfjG%2BSv2SfWienTUPxNbet--IcU1rC%2FllNpGjdmt--fDb%2BQJ46KtzJ83f02sOHXQ%3D%3D')
#
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
# }
#
# jia = RequestsCookieJar()
# for cookie in cookies.split(';'):
#     key,value = cookie.split('=',maxsplit=1)
#     jia.set(key,value)
#
# try:
#     res = requests.get('https://github.com/',cookies=jia,headers=headers,verify=False)
# except Exception as e:
#     print(e)
# else:
#     # save_file('资料文件\\github.html',res.text)
#     print(res.text)



# requests.get('https://www.httpbin.org/cookies/set/number/123456789')
# r = requests.get('https://www.httpbin.org/get')
# print(r.text)


# s = requests.Session()
# s.get('https://www.httpbin.org/cookies/set/number/123456789')
# r = s.get('https://www.httpbin.org/get')
# print(r.text)


# from requests.auth import HTTPBasicAuth
# auth = HTTPBasicAuth('admin','admin')
# res = requests.get('https://ssr3.scrape.center/',auth=('admin','admin'))
# print(res.text)


# proxies = {
#     'https:':'http://39.106.165.196:8080',
#     'http:': 'http://39.106.165.196:8080',
# }
# res = requests.get(url_hp_g,proxies=proxies)
# print(res.text)


e = requests.Session()
r = Request(method='GET',url=url2_lz,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',})
prepared = e.prepare_request(r)
res = e.send(prepared)
print(res.cookies)
