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


# response = request.urlopen(url='http://jwxt.jxsdky.edu.cn:8081/cas/login.action')
# response_header = response.getheaders()
# for i in response_header:
#     print(i)


# str1 = '我的使劲儿'
# print(bytes(str1,'utf-8'))

# data = bytes(parse.urlencode({'name':'germey'},encoding='utf-8'),'utf-8')
# response = request.urlopen(url='https://www.httpbin.org/post',data=data)
# response_body = response.read().decode('utf-8')
# print(response_body)



# try:
#     response = request.urlopen(url='https://www.httpbin.org/get', timeout=10)
# except error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('超时访问')
# else:
#     response_body = response.read().decode('utf-8')
#     print(response_body)


# url = 'https://www.httpbin.org/post'
# data = bytes(parse.urlencode({'name':'germey'},encoding='utf-8'),'utf-8')
# header = {
#     'User_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
#     'Host':'www.httpbin.org'
# }
# request_message = request.Request(url=url,data=data,headers=header,method='POST')
# request_message.add_header('User-Agent','Mozella/4.0 (compatible; MSIE 5.5;Windows NT)')
# res = request.urlopen(request_message)
# print(res.read().decode('utf-8'))


# 使用高级用法
# (一)验证
# url = 'https://ssr3.scrape.center/'
# username = 'admin'
# password = 'admin'
#
# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None,url,username,password)
#
# auth_handler = HTTPBasicAuthHandler(p)
#
# opener = build_opener(auth_handler)
#
# try:
#     res = opener.open(url)
# except error.URLError as e:
#     print(e.reason)
# else:
#     result = res.read().decode('utf-8')
#     print(result)


# （二）代理
# proxy_handler = ProxyHandler({
#     'http': 'http://43.199.3.39:8080',
#     'https': 'https://43.199.3.39:8080'
# })
#
# opener = build_opener(proxy_handler)
#
# try:
#     res = opener.open('https://www.baidu.com/')
# except error.URLError as e:
#     print(e.reason)
# else:
#     print(res.read().decode('utf-8'))


# (三)cookie
# cookie = CookieJar()
# cookie_handler = HTTPCookieProcessor(cookie)
# opener = build_opener(cookie_handler)
# try:
#     res = opener.open('https://baidu.com')
# except error.URLError as e:
#     print(e.reason)
# else:
#     for i in cookie:
#         print(i.name,"=",i.value)


# file = '资料文件\\cookie.txt'
# cookie = cookiejar.MozillaCookieJar(file)
# handler = HTTPCookieProcessor(cookie)
# opener = build_opener(handler)
# try:
#     res = opener.open('https://baidu.com')
#     for i in cookie:
#         print(i.name,"=",i.value)
# except error.URLError as e:
#     print(e.reason)
# else:
#     cookie.save(ignore_discard=True,ignore_expires=True)


# file = '资料文件\\cookie2.txt'
# cookie = cookiejar.LWPCookieJar(file)
# handler = HTTPCookieProcessor(cookie)
# opener = build_opener(handler)
# try:
#     res = opener.open('https://baidu.com')
#     for i in cookie:
#         print(i.name,"=",i.value)
# except error.URLError as e:
#     print(e.reason)
# else:
#     cookie.save(ignore_discard=True,ignore_expires=True)


# cookie = cookiejar.LWPCookieJar()
# cookie.load(filename='资料文件\\cookie2.txt',ignore_discard=True,ignore_expires=True)
# handler = request.HTTPCookieProcessor(cookie)
# opener = build_opener(handler)
# res = opener.open('https://www.baidu.com')
# print(res.read().decode('utf-8'))


# try:
#     request.urlopen('https://cuiqingcai.com/404')
# except error.URLError as e:
#     print(e.reason)


# try:
#     request.urlopen('https://cuiqingcai.com/404')
# except error.HTTPError as e:
#     print(e.reason,e.code,e.headers,sep='\n\n')


# try:
#     request.urlopen(url3_bu,timeout=0.01)
# except error.URLError as e:
#     print(e.reason)
#     print(type(e.reason))
#     if isinstance(e.reason,socket.timeout):
#         print('ture')


# url = parse.urlsplit('https://www.bilibili.com/video/BV1FNgN6rExw/?spm_id_from=333.1007.tianma.1-1-1.click')
# print(url)
# result1 = parse.urlunsplit(['https','www.bilibili.com','index','a=6',''])
# print(result1)


# url = parse.urlsplit('https://www.bilibili.com/video/BV1qnuq6dEga/?spm_id_from=333.1007.tianma.3-3-9.click')
# data = parse.parse_qs(url)
# print(data)


# value1 = '当孤僻之人遇到青春生活'
# params = {
#     'wd':value1
# }
# url_list = list(parse.urlsplit(url3_bu))
# url_list[2] = '/s'
# url_list[3] = parse.urlencode(params)
# url_list[4] = ' '
# print(url_list)
# url = parse.urlunsplit(url_list)
# print(url)


# word = parse.quote('壁纸')
# url = 'https://www.baidu.com/s?wd=' + word
# print(url)


# username = '2402099172'
# password = 'Aa@1901420817'
#
# cookie = cookiejar.MozillaCookieJar()
# handler_cookie = HTTPCookieProcessor(cookie)
#
# ps = HTTPPasswordMgrWithDefaultRealm()
# ps.add_password(None,'http://jwxt.jxsdky.edu.cn:8081/cas/login.action',username,password)
# handler_ps = HTTPBasicAuthHandler(ps)
#
# opener = build_opener(handler_cookie,handler_ps)
# try:
#     res = opener.open('http://jwxt.jxsdky.edu.cn:8081/cas/login.action',data=bytes(parse.urlencode({'username':username,'password':password},encoding='utf-8'),'utf-8'))
# except error.HTTPError as e:
#     print(e.reason)
# else:
#     with open('资料文件\\校园网站.html','w',encoding='gbk') as f:
#         f.write(res.read().decode('gbk'))
#     cookie.save('资料文件\\学校cookies.txt')


# bilbil_robots = robotparser.RobotFileParser('https://www.bilibili.com/robots.txt')
# bilbil_robots.read()
#
# result2 = urlopen('https://www.baidu.com/robots.txt').read().decode('utf-8').split('\n')
# bilbil_robots.parse(result2)
# result = bilbil_robots.can_fetch('BaiduSpider','https://www.bilibili.com/index.html')
# print(result)