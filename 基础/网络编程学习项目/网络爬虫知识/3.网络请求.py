from urllib import request
from urllib import parse
import requests
from http.cookiejar import CookieJar
#中的urllib库中的知识详解。

# urllib 库介绍：
# 基本信息：urllib 是 Python 3 自带的基本网络请求库，无需安装，可直接在代码中使用。
# 功能特点：能模拟浏览器行为，向服务器发送请求并保存返回的数据。
# 模块变化：Python 3 将所有网络请求相关方法集成到 urllib.request 模块下，与 Python 2 版本不同。
# urllib库由四个模块组成
#     request模块：打开和浏览URL中的内容
#     error模块：包含urllib.request发生的错误或异常
#     pares模块：解析URL
#     robotparser模块：解析robots.txt文件
# 第一个模块：request模块，打开和浏览URL中的内容


'''
urlopen 函数基本使用：
    导入模块：需从 urllib.request 模块导入使用。
    打开网站并读取数据：以打开百度网站为例，使用 request.urlopen指定URL发送请求，
    得到响应对象后调用 read 方法可读取网页代码数据。
    请求优势：用 Python 代码实现请求只需一行，体现了 Python 写爬虫的便捷性。
    代码运行结果：运行代码可打印出百度网页的源代码，虽与浏览器右键查看的代码可能有差异，
    原因可能是缺少 cookie 信息或百度做了处理。
urlopen 函数参数及返回值：
    参数说明：除 URL 外，还可传递 data和timeout参数。传递data时走post请求，默认走get请求；timeout可指定超时时间。
    返回值类型：(返回 http.client.HTTPResponse 类文件句柄对象。)
返回对象方法使用：
    read 方法：默认读取所有数据，也可指定读取字节数。
    readline 方法：只读取一行数据。
    readlines 方法：将网页数据以多行形式读取，每行作为列表中的一项。
    getcode 方法：获取当前请求返回的状态码，状态码为 200 表示请求正常。
'''

def get_html(new_file,resource):
    with open(f'{new_file}.html','w+',encoding='utf-8') as file:
        file.write(resource)

# 一。urlopen的使用
#  发送请求
# url = "https://www.baidu.com/"
# reap = request.urlopen(url)
# #urlopen（）函数返回的是一个HTTPResponse对象
# print(reap)                               #：输出reap对象，这可能是一个HTTPResponse对象
# print(reap.read().decode('utf-8'))        #以utf-8格式进行文件编码（将二进制的字符串解码为utf-8字符串，并读出页面源代码）
# i = reap.read().decode('utf-8')
# with open('baidu.html', 'w', encoding='utf-8') as file:
#     file.write(i)
# print(reap.geturl())                      #：获取最终的URL。所获得的是二进制的编码需要用到decode('utf-8')进行转变
# print(reap.msg)                           #：获取状态消息
# print(reap.status)                        #：获取HTTP状态码。
# print(reap.version)                       #：获取HTTP版本。
# print(reap.reason)                        #：获取原因短语


#抓取二进制文件
# url = "https://www.baidu.com/img/bd_logo1.png"
# reap = request.urlopen(url)
# picture = reap.read()
# with open("D:/文件资源(word,ppt,excel)/新建文件夹/baidu.png",'wb') as file:
#     file.write(picture)


# 二.运用request中的Request类：
"""实战：【用Requset爬取拉钩网职位信息】"""
# url = 'https://www.lagou.com/homepage/promotions.json?seoSubSite=%E5%85%A8%E5%9B%BD'
# # result = request.urlopen(url)
# # print(result.read())
# '''用于有反爬装置所以查到的是无用信息，运用Request类中的方式进行查找'''
# # Request不仅可以传递headers，还可以传递method/data。
# header = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
#     "Refere":'https://www.lagou.com/wn/'
# }        #传递headers
# date = {
#     'seoSubSite': '全国'
# }       #负载中的信息参数
# reap = request.Request(url,headers=header,data=parse.urlencode(date).encode('utf-8'),method='GET')
# #进行post请求时，数据应该是:字节(bytes)\字节可迭代对象\或者文件对象，所以要将字符串数据编码为字节，如使用str.encode（）方法
# reault = request.urlopen(reap)                     #借助urlopen发送
# html1 = reault.read().decode('utf-8')
# # print(html1)
# # print(reault.status)
# with open('html2.html','a+',encoding='utf-8') as file1:
#     file1.write(html1)


'''
urlretrieve 函数介绍：
    功能：可以方便地将服务器上的文件下载到本地，相比 PHP、Java 等语言，Python 使用该函数只需一句代码即可实现文件下载。
    参数：第一个参数是要下载文件的 URL，第二个参数是文件下载到本地的路径及文件名。
下载网页示例：
    操作步骤：在 Python 中使用 URL retrieve 函数，指定百度首页 URL（www.baidu.com），并将下载文件命名为 “百度.html”，执行代码后即可完成下载。
    效果验证：运行代码后，本地会生成 “百度.html” 文件，打开该文件虽然部分内容因通过 file 文件打开无法加载，但与百度网页基本相似。
下载图片示例：
    操作步骤：在百度搜索王者荣耀鲁班图片，右键复制图片地址，在 Python 代码中使用 URLretrieve 函数，将图片地址作为第一个参数，文件名改为 “鲁斑.jpg”，保存代码并运行。
    效果验证：运行代码后，图片文件会立即下载到本地，双击可查看下载的图片。
函数在爬虫程序中的应用：
    获取图片 URL：在爬虫程序中，可以使用爬虫去获取网站上所有图片对应的 URL。
    批量下载图片：获取到图片 URL 后，再通过 URL retrieve 函数可以一次性将所有图片下载下来。
'''
# 【urlretrieve函数的使用】
url = "https://m.yangshipin.cn/portrait_video?vid=z000058kljs"
request.urlretrieve(url,"D:/文件资源(word,ppt,excel)/新建文件夹.mp4")


#关于urllib库中的parse模块：
"""
函数介绍 ：
    urlencode 函数 ：用于将查询字段进行编码，因为 URL 中除英文字母、数字和部分符号外的数据都需编码才能发送。
    parse_qs 函数 ：与 urlencode 函数功能相反，可将编码后的参数还原成原来的模样。这两个函数都在urllib.parse模块中。
urlencode函数用法示例（本地编码） ：
    定义查询字段 ：定义一个字典dict1，包含name（值为 “张三”）、age（值为 18）、grade（值为 “hello world”）等查询字段。
    进行编码 ：使用urllib.parse.urlencode(dict1)对查询字段进行编码，得到编码后的结果。
    查看结果 ：打印编码结果，中文会以百分号加十六进制形式编码，***【空格会用加号区分，两点号以等号表示，逗号以&表示】
urlencode函数实际应用（请求 URL） ：
    直接请求报错 ：尝试直接请求包含中文的 URL（如搜索 “刘德华” 的百度 URL），会因urllib底层使用 ASCII 码编码而报错。
    正确请求步骤 ：定义参数params字典，将wd对应的值设为 “刘德华”；使用urllib.parse.urlencode(params)对参数进行编码得到qs；
    将编码后的qs拼接到 URL 后面，拼接时要在前面加上问号；用拼接好的正确 URL 进行请求并读取数据，可获取网页正常数据。
parse_qs函数用法示例 ：
    先编码 ：将查询字段进行编码得到编码后的字符串qs。
    再解码 ：使用urllib.parse.parse_qs(qs)对编码后的字符串进行解码，将结果存储在result中。
    查看对比 ：打印编码后的qs和解码后的result进行对比，解码结果会将数据放在列表中，与原数据基本相同。
"""


#【urlencode函数、parse_ps函数】
from urllib import parse
import requests
# dic1 = {"name":'缪泽平','age':20,'greet':'hello world'}
# jie = parse.urlencode(dic1)   #进行解码：urlencode()
# print(jie)                    #打印经解码后的数据(用于转化汉字)
# bian = parse.parse_qs(jie)    #进行编码：parse_ps()
# print(bian)                   #把起转化成汉字
# url = "https://www.baidu.com/s"
# name = input('请输入你要查找的人物: ')
# name_encode = {"wd":name}
# name_jie = parse.urlencode(name_encode)
# url = url + '?' + name_jie
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0"
# }
# reap = request.urlopen(url)
# i1 = reap.read().decode('utf-8')
# il = request.Request(url,headers=headers)
# result = request.urlopen(il)
# print(result.read().decode('utf-8'))
# get_html('html01',i1)
# reap = requests.get(url,headers=headers)
# print(reap.text)


'''
会议讨论了 Python 中 URL 解析的相关内容，包括 URL 解析的概念、使用的函数以及函数间的区别等，具体如下：
课程内容介绍：
承接上节课：上节课讲解了参数的编码和解码函数，本节课讲解 URL 解析的两个函数。
URL 解析含义：将 URL 分成 scheme（协议）、host（域名）、port（端口）、path（路径）、params（参数）、查询字段以及锚点等部分。
代码编写准备：
导入模块：从 “urllib” 模块导入 “parse” 子模块，因为 URL 解析相关函数在该模块下。
URL 解析示例：
定义 URL：定义一个示例 URL，如 “https://www.baidu.com/s;hello?wd=Python&username=ABC#a”。
使用 urlparse 解析：使用 “parse.urlparse” 函数将 URL 传入，用变量 “result” 接收解析结果，
                  可打印 “result” 获取完整解析信息，也可通过 “result.scheme”“result.netloc” 等属性获取单个部分信息。
使用 urlsplit 解析：使用 “parse.urlsplit” 函数达到同样的 URL 分割效果，用变量接收解析结果后可进行打印查看。
两个函数区别：
urlparse 特点：“urlparse” 函数解析结果多了一个 “params” 属性，该属性数据位于查询字段前的分号后到问号之间，不过在爬虫和网站开发中基本用不到。
urlsplit 特点：“urlsplit” 函数解析结果没有 “params” 属性，无法获取对应部分数据。
使用建议：两个函数基本功能一样，使用哪个均可，只需知道 “urlparse” 多了 “params” 属性。
params 属性说明：
与查询参数对比：“params” 和问号后面的查询参数本质都是给服务器发送数据，语义上有区别，但实际使用区别不大，且使用较少
'''
# 2.urlparse函数和urlsplit函数的用法
# url = 'https://www.baidu.com/s;hello?wd=Python&username=ABC#a'
# print(parse.urlparse(url))
# print(parse.urlsplit(url))


# #查找电脑外网的ip地址
# url = "http://httpbin.org/get"
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
#     "Host":"ttpbin.org"
# }
# result = request.Request(url,headers=headers,method='GET')
#
# reap = request.urlopen(result,timeout=20)
# print(reap.read().decode('utf-8'))  #没有使用代理ip


# 【使用代ProxyHandler设置代理ip】
#1.使用ProxyHandler,传入代理构建一个handler
# handler = request.ProxyHandler({"http":"127.0.0.1:8000"})
# #2.使用上面创建的handler构建一个opener
# opener = request.build_opener(handler)
# #3.使用opener去发送一个请求
# reap1 = opener.open(url)
# print(reap1.read())
# sd = reap1.read().decode('utf-8')
# get_html('html02',sd)
# handler = request.ProxyHandler({'http':'47.96.252.117:80'})
# opener = request.build_opener(handler)
# request.install_opener(opener)
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
#     "Host":"ttpbin.org"
# }
# rep = request.Request(url,headers=headers,method='GET')
# reap1 = request.urlopen(rep)
# print(reap1.read().decode('utf-8'))


###ProxyHandler处理器(代理):
# 1.代理的原理:在请求目的网站之前,先请求代理服务器,然后让代理服务器去请求目的
#   网站,代理服务器拿到目的网站的数据后,再转发给我们的代码
# 2.http://httpbin.org:这个网站可以方便的查看http请求的一些参数。
# 3.在代码中使用代理:
# 使用`urllib.request.ProxyHandler',传入一个代理,这个代理是一个字典,字
# 的key依赖于代理服务器能够接收的类型,一般是`http`或者`https",值是"ip:port"(‘IP地址：端口号’)
# 使用上一步创建的"handler",以及"request.build_opener"创建一个"opener对象。
# 使用上一步创建的"opener",调用"open"函数,发起请求。
# 示例代码如下:
    #from urllib import request
    # url = 'http://httpbin.org/ip'
    # # 1.使用ProxyHandler,传入代理构建一个handler
    # handler = request.ProxyHandler({"https": "47.96.42.206:80"})
    # # 2.使用上面创建的handler构建一个opener
    # opener = request.build_opener(handler)
    # # 3.使用opener去发送一个请求,调用open（）函数。
    # resp = opener.open(url)
    # print(resp.read())

"""
会议讨论了爬虫课程中 proxy handler 代理处理器的相关知识，包括其作用、原理、代码实现以及代理服务商的选择等内容，具体如下：
反爬虫机制背景：
IP封禁原因：爬虫若用同一 IP 在短时间内频繁请求网站数据，网站服务器通过访问日志和流量统计监测后，会将该 IP 加入黑名单，导致爬虫无法获取数据。
应对措施：  使用 Python 中的 proxy handler 处理器，让爬虫在发送请求时使用代理，解决 IP 被禁问题。
代理原理：
    正常请求模式：电脑 IP 直接向百度服务器请求数据，若因频繁请求被服务器识别为爬虫，IP 会被封，后续请求无响应或收到错误数据。
    代理请求模式：电脑先访问代理服务器，代理服务器用自身 IP 向百度发送请求，百度接收请求后会认为是正常请求，将数据返回给代理服务器，再由其返回给电脑，实现间接获取数据。
proxy handler 代码实现步骤：
创建代理字典：使用 request 下的 proxy handler，传入字典形式的代理，字典 key 为代理支持的请求方式（如 HTTP、HTTPS），value 为代理服务器的 IP 地址和端口号。
创建 opener：通过 request 下的 build_opener 工厂方法，将创建好的 handler 传入，得到 opener 对象。
发送请求：调用 opener 的 open 方法，传入 URL 发送请求并获取响应。
代理服务商情况：
    西刺免费代理：所有代理免费，但 IP 不稳定，不建议在公司写爬虫时使用。
    快代理：有免费和付费代理，免费代理不稳定、响应速度慢，建议公司使用付费代理。
    代理云：与快代理类似，有免费和付费服务。
测试代理效果：
测试网址选择：选择 httpbin 网址测试代理，该网址可打印当前电脑外网 IP 地址。
测试方案：一是不使用代理向该网址发送请求，打印当前 IP；二是使用代理向该网址发送请求，对比使用代理前后的 IP 地址，以验证代理效果。
"""


# 8~9.cookie原理和格式详解—~cookie的应用
"""
什么是cookie:
在网站中,http请求是无状态的。也就是说即使第一次和服务器连接后并且登录成功后,第二次请求服务器依然不能知道当前请求是
哪个用户。cookie的出现就是为了解决这个问题,第一次登录后服务器返回一些数据(cookie)给浏览器,然后浏览器保存在本
地,当该用户发送第二次请求的时候,就会自动的把上次请求存储的cookie数据自动的携带给服务器,服务器通过浏览器携带的回数
据就能判断当前用户是哪个了。cookie存储的数据量有限,不同的浏览器有不同的存储大1,但一般不超过4KB。因此使
用cookie只能存储一些小量的数据。
cookie的格式:
[Set-Cookie: NAME=VALUE: Expires/Max-age=DATE: Path-PATH: Domain-DOMAIN_NAME: SECURE]
参数意义:
NAME:cookie的名字。
VALUE:cookie的值。
Expires:cookie的过期时间。
Path:cookie作用的路径
Domain:cookie作用的域名。|
SECURE:是否只在https协议下起作用。
"""


# 鹏主页:http://www.renren.com/880151247/profile
# 人人网登录url:http://www.renren.com/PLogin.do
#1.使用cookie去请求大鹏的页面
# url = "https://pan.baidu.com/disk/main?_at_=1751865116247"
#
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
#                  '(KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
#     "Cookie":"XFI=d684a6e2-6ff1-1a9c-d459-1cdacb6d46e1; XFCS=778DFAE6F3D5110AC551082925EF252578436EDB65
#     D369FF69A7739C474D316F; XFT=MGxLH/JvA7sN76uJ21KJMfNQGTW5XPguUpijzWmu51Q=; BIDUPSID=BC707AB53F7FB31C
#     9939835376A5E48A; PSTM=1727859230; PANWEB=1; Hm_lvt_d5bdc9eee733100f7b952fc44f7e53e4=1737186261;
#     Hm_lvt_fa0277816200010a74ab7d2895df481b=1737279772,1738769180; Hm_lvt_f5f83a6d8b15775a02760dc5f490
#     bc47=1738803441; H_WISE_SIDS_BFESS=61027_61667_61985_62080_62055_62067_62093_62112_62125_62156_62168;
#     Hm_lvt_0ba7bcf57b5e55fbfbab9a2750acdf3e=1746511652,1747404071,1747404103,1749051121; BAIDUID=32D3E2A
#     38EFD251DD14B84FA2D00284F:FG=1; newlogin=1; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1751446361,1751
#     450777,1751454708,1751458439; BDCLND=N4MD81lkXVQC4%2FGrK%2F2OjoiVPKf5Vp8zZmYuup23Mwc%3D; H_WISE
#     _SIDS=110085_632160_636706_632291_632701_640917_641938_644665_644679_646538_646544_651479_651899_6
#     52165_650475_652590_645235_653266_653823_654291_654560_654770_654754_654779_655339_655445_655724_65563
#     6_652296_656107_656103_656101_656093_656203_656405_656456_656449_656503_656506_656657_656664_656514_65
#     6703_655076_654309_654943_654341_657116_657126_657100_657056_657225_655951_641262_656736_657521_657519_
#     657809_656497_657675_657870_658000_657787_657997_657501_658028_658031_658033_658066_658095_658124_658055
#     _658256_658257_658007_658453_658448_658473_656755_655416_657854_658506_656077_658547_658531_656172_658
#     573_656626_658594_658589_658086_658581_658582_656765_658637_658586_658791_658798_658752_658886_658923_
#     658929_658921; H_PS_PSSID=62327_63144_63324_63582_63626_63689_63693_63725_63714_63776_63796_63815_63825
#     _63881_63895_63904_63949_63948; BAIDUID_BFESS=32D3E2A38EFD251DD14B84FA2D00284F:FG=1; ZFY=YlqBUaA02G56RDUU
#     oxWYf6iPGvnj:AyGS55RVYgvks:A8:C; BA_HECTOR=0la180aha0a58ga18gah2g24a1ag001k6maqr25; csrfToken=UC3gBhuS-OeB0
#     ZSrF0vbBZpI; ppfuid=FOCoIC3q5fKa8fgJnwzbE67EJ49BGJeplOzf+4l4EOsgA3km/7mieS5OWtjjPv0Tl3Nlhu3Url0RbXxAWtqk
#     bWF7e7ZlgnHadyyuWCY/uMxlhySjgWcwFfWfIqud05MkOpFu6mymyRJff9LTSrWHKTRv7LsroVl4YX/BReUyYf6p84mfaqx2MMpvaMn
#     IuFMDwWZbgLHt5TE13pLY+pFG/9M13v7KVHDQkHFzclTu0xsBL3FBMCGQiVDprMNeg5jFhbBWioGGwmMoeBMVNwqqLICU2CgaocfeStYRK
#     2bRvyzBdBHKc5Tb7hfuvNlP6KCKSEafKHG3PabitT+i2ChRTW/aLCPXd1oz71pYnkYkJC79JRsXmNXkBTLP+MGIiApU5toMIeBYlkfdmt
#     MZgeaLtckH3PfLajwqrF6nlcEKy7B/oyXfOQZ1Cb/GKSVrqy1qwLxh5NPfvlaawGT22E/mOZn0yF2uxbNJYXLisdCIKKe81cgRbanCPgF
#     cg1I0Ws80f08JWJ17URNUrnVqDpBoQUxvv4kVbE0agDQk2K/qEJvSCRemQSkhKLq1UeH6GxCJ+MAIYbPQxssj0AC629A2Yui9ATwOutSQ4
#     9JZmSIHAhS/GidIZLaWCI1kHGAr81p3o/ex+/K9iHJc3DGbpLMf46NrWXpzL26g/vLjjogtrUIsQ5pXWMOQaiSw2FG2fsHVU+i83VNFTT
#     iouuYQK4MYwFVHi+WHLwOplDX8tQRD2aszVdNKEy7xjrPuZyMgTHRJGGkxaEyjww1bXQjv2tiIRmqPhwW3AN0n9RlprqIAy3Kj5ut/8t
#     HvAKkd5km0nfYk3sgqJo1V5ktaW5/9ZpOtVx7X8yhzQe9KckkJ5EqMnX34kilDqdVbEvi8vfiLqZ/MviEtdwYDCb9uUYJqPaqqVYSwG
#     34zuVk8yAyO5tKVjmLYEUMUQj8VEb8yZC4O2lvQEueo+vuCaXBMaB83ijspIA6KF6KHtnw7RT5b2WYawT3FCxkJS/t4n+X6SgRupF
#     NaxkQoR54T7iXiCgAj14lbpYvSLUSxJHW9Zi8TRwJN7icvPGF/0X/7ClI0dds8UUw8cSTQyUvg5bG6rt5+COubo5Yv960PGZNTI5kzr
#     M/fpE6jjOLqbJ0OiFqv83mUyLTAoB6UIboa+Iqe94aJ7s6CYIHtXKlgRWL6WmwD0zhEUzj9ZJseUlzwEV+bscicwIjSCwQvM4e3xn
#     zVzlld+zvYOxBeAYXcqNbm/K33IR8l2pINxW6hKjOiZkR6pMEYUiULZn334RIiR13WV4E4pKcUs0bM3mLxclwj0rieaMqDoKAjylxPH1
#     +91jmdJgJRdZn; XFI=065a1dc0-5af2-11f0-b8f7-71aa818493a4; XFCS=124CA0CB4ECA7A4D075D6480D048F5EC10EABE
#     FB1059ECF82CBD658AB4E09258; XFT=An3YOMS/scHuuMOwXx/eepbcDs33QCwCNRrDzAYIHmE=; BDUSS=IxZXRlZzI0LWdac2
#     9HZjhWRklTa3FVNmhnYzh4bkxSfn5XZ05xc1Uta1E1cEpvSVFBQUFBJCQAAAAAAQAAAAEAAAAuQK2O17fC~tChz8i35gAAAAAAAAAA
#     AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBZa2gQWWtoRD; BDUSS_BFESS=IxZXRlZzI0LWdac
#     29HZjhWRklTa3FVNmhnYzh4bkxSfn5XZ05xc1Uta1E1cEpvSVFBQUFBJCQAAAAAAQAAAAEAAAAuQK2O17fC~tChz8i35gAAAAAAAAAAA
#     AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBZa2gQWWtoRD; STOKEN=1282c359cb8eb629335565
#     ad35f3537536a63073196113236121469d39b0465f; PANPSC=15629356902539681178%3AnHZOtuqy9avbHKVEd7VA2lcS2d9ns
#     3O5C61tf8
#     CKQkgsrQbf%2F9OrcKUY4cQrI%2BJ7z81ttRoL0tCAzpMjKfHvSigbb3uMK6YP14SxOx5WiCpCNDWYUdN3xXW236T0Jqd
#     7BYuwRMPExkvncjoc%2Bq5tcK34yop26WlusG7YZLnfZ%2BWv%2BjYtLTMR3v%2Fj5saXbmrfOBBjRPX30t47r%2BPehKJmBmb70IK
#     5h5Mbm8zeXLiuuhx%2FceuZlCBNxGdrQNeIu%2BZmjoV20S1sm8jpn6AUYnG4VhWFGB9e3Q2UT1j18OHJVxqfZb8774pAupKxVlqrI
#     DxM; Hm_lvt_182d6d59474cf78db37e0b2248640ea5=1751448788,1751865081,1751865396,1751865619; Hm_lpvt_182d
#     6d59474cf78db37e0b2248640ea5=1751865876; ndut_fmt=B01317AE2790CA564535450095B051FDF835795C21E2C3C00180
#     BC82BB72AD42; ab_sr=1.0.1_M2FkMzJlZDJlOWQyN2FlN2IxMWJkNzQ0ZGJhNGRjYWNkMDg5NDEzYTMyM2JjZTZhMjRkNDI3ZWFmZ
#     WY0Y2EzZTkxMzdjOTE2NmEyNWYyMmUzMWE5MjdhYWJlOTc2ZDU1ZWU0M2U5NzZmZDA0NTYyNTcwOWQzYWYyOTU2MWYzNGM0ZTg3YzUxY
#     WVlYmJhYmIzZDI4YTAyNzEzMjU5MDUzZjNiNjMwZWQzMDljMzQ5MDUxMDYxZTc3ZmY4Njk2ZWU5"
# }
# rep = request.Request(url=url,headers=headers)
# reap = request.urlopen(rep)
# #print(reap.read().decode('utf-8'))  #注意reap.read()使byte形式
# with open('xuexiao1.html','w',encoding='utf-8') as file1:
#     # write函数必须写入一个str的数据类型
#     # 注意reap.read()读出来的使byte数据类型
#     # bytes -> decode -> str 解码
#     # str ->encode -> bytes  编码
#     file1.write(reap.read().decode('utf-8'))


# 10.实战-爬虫自动登录访问授权页面
# from urllib import request
# from http.cookiejar import CookieJar
# from urllib import parse
# url = "https://www.hikarinagi.net/"                        #url = "https://www.bilibili.com/"
# # #https://www.hikarinagi.net/
# url2 = "https://www.hikarinagi.net/galgamer/116732"        #url2 = "https://space.bilibili.com/3546718589160056?spm_id_from=333.1007.0.0"
# # #https://www.hikarinagi.net/galgamer/116732
# #1.登录
# # 1.1创建一个CookieJar对象来存储cookie
# cookie = CookieJar()
# # 1.2创建一个HTTPCookieProcessor处理器，并将cookiejar（通过变量命名后为cookie）传递给它
# handler = request.HTTPCookieProcessor(cookie)
# # 1.3创建一个自定义的opener，包含cookie处理器(即为handler)
# opener = request.build_opener(handler)
# # 1.4使用opener发送登录的请求（包含账户和密码）,他会自动处理cookie
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
#                  "(KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0"
# }
# date = {
#     "email":'wyys22@qq.com',
#     "password":"A1901420817"
# }
# rep = request.Request(url,headers=headers,data=parse.urlencode(date).encode('utf-8'))
# #用这个opener发送请求，他会自动处理cookie
# opener.open(rep)
# #可以打印出存储在CookieJar中服务器返回的cookie值。
# for cookie1 in cookie:
#     print(f"Cookie: {cookie1.name} = {cookie1.value}")
# # 2.访问个人主页
# # 获取个人主页的页面的时候，不要新建一个新的opener
# # 因该使用之前的那个opener，因为之前的那个opener已经包含了登录所需要的cookie信息
# rep2 =request.Request(url2,headers=headers)
# reap = opener.open(rep2)
# #写入文件中
# with open('hikarinagi.html',"w",encoding="utf-8") as fg:
#     fg.write(reap.read().decode('utf-8'))


# 11.cookie信息的加载与保存
# 保存cookie到本地，用http.cookiejar模块中的MozillaCookieJar
# from urllib import request
# from http.cookiejar import MozillaCookieJar
# cookie = MozillaCookieJar('cookie1.txt')
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# url = 'http://httpbin.org/cookies/set?course=abc'
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0"
# }
# req = request.Request(url, headers=headers)
# # 1. 先发起请求，让 Cookie 容器获取服务端返回的 Cookie
# response = opener.open(req)
# # 2. 再保存 Cookie 到文件（此时 cookie 里已有数据）
# cookie.save(ignore_discard=True)
# # 如需加载，后续可执行 load（实际场景一般是“下次运行代码时加载”，按需使用）
# # cookie.load(ignore_discard=True)
# for i in cookie:
#     print(i)
# #设置URL
# url = "https://dm.xifanacg.com"
# url1 = f"{url}/user/index.html"  # 登录页面
# url2 = f"{url}/user/login.html"   # 登录API
# #创建Cookie处理器
# cookie = CookieJar()
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# #设置请求头
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
#     "Referer": url1,  # 添加Referer头，模拟浏览器行为
#     "Origin": url
# }
# # 先访问登录页面，获取可能的初始Cookie
# req1 = request.Request(url1, headers=headers)
# opener.open(req1)
# # 准备登录数据
# data = {
#     "account_name": "18379309798",
#     "password": "A1901420817",
#     "remember": "1"  # 添加记住登录状态参数
# }
# # 发送登录请求
# req2 = request.Request(url=url2, headers=headers, data=parse.urlencode(data).encode('utf-8'), method='GET')
# response2 = opener.open(req2)
# # # 检查登录响应
# # result1= response2.read().decode('utf-8')
# # 登录后访问主页
# # home_url = f"{url}/index.html"
# # req3 = request.Request(url=home_url, headers=headers,method="GET")
# # result2 = opener.open(req3)
# # result2_jie = result2.read().decode('utf-8')
# # 保存结果
# with open('zhuye.html', 'w', encoding='utf-8') as f1:
#     f1.write(response2.read().decode('utf-8'))

# with open('home_page.html', 'w', encoding='utf-8') as f2:
#     f2.write(home_content)





# 重中之重{[【request库的使用方法】]}
#发送get请求
# url = "http://www.baidu.com/s?"
# response = requests.get(url)
# # 【*】requests常见的属性和方法：
# print(response.text)             #打印响应内容 == response.content.decode(‘猜的’)
# # 注意这里!
# print(response.content.decode())    #response.content返回的时bytes类型，可以进行decode操作
# print(response.url)                 #打印响应的ur1
# print(response.status_code)         #打印响应的状态码
# print(response.request.headers)     #打印响应对象的请求头
# print(response.headers)             #打印响应头
# print(response.request._cookies)    #打印请求携带的cookies，返回cookieJar类型
# print(response.cookies.get_dict())  #打印响应中携带的cookies


#  【**】返送带参数的请求
# 添加请求头和字符串参数（headers、params）
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0'
# }
# keyword1 = input('百度一下你就知道：')
# params = {
#     'wd':keyword1
# }       #设置参数
# result = requests.get(url=url,headers=headers,params=params) #params用于在get请求中传递查询的字符串，                                                          #这些参数会被附加到 URL 的末尾，不需要进行编码因为requests会自动进行。
# with open('baidu1.html','w',encoding='utf-8') as fg:
#     fg.write(result.content.decode('utf-8'))


# 【***】在headers中添加cookie
# url2 = "https://www.acfun.cn/member/"
# headers = {
#     'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#                  "AppleWebKit/537.36 (KHTML, like Gecko) Chr"
#                  "ome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
#     'Referer':'https://www.acfun.cn/',
#     'Cookie':'_did=web_77064771BFAB3B2; _did=web_77064771BFAB3B2; '
#              'csrfToken=sG4EBk1cTd7yEeuT4arCuYCF; webp_supported=%'
#              '7B%22lossy%22%3Atrue%2C%22lossless%22%3Atrue%2C%22al'
#              'pha%22%3Atrue%2C%22animation%22%3Atrue%7D; Hm_lvt_2a'
#              'f69bc2b378fb58ae04ed2a04257ed1=1752039620; HMACCOUNT'
#              '=B84C1BE8616827D0; lsv_js_player_v2_main=ca85g8; auth'
#              '_key=76349226; ac_username=%E9%95%BF%E4%B9%88; ac_use'
#              'rimg=https%3A%2F%2Fimgs.aixifan.com%2Fstyle%2Fimage%2'
#              'FdefaultAvatar.jpg; cur_req_id=3052682980E59E28_self_'
#              '06166551a58835218309b3d9939687ce; cur_group_id=305268'
#              '2980E59E28_self_06166551a58835218309b3d9939687ce_0; s'
#              'tochastic=cWNkZ2x6cGIyYg%3D%3D; acPasstoken=ChVpbmZyY'
#              'S5hY2Z1bi5wYXNzdG9rZW4ScOfEGhdInyntXu2NtEHT0DjazLuMYRx'
#              'BXY_KLwTlUX7UMGFcGu1DaV2c2gkPo7SLHZr1Ys1Hm79pSAkWbGgt5'
#              'tBip7kN3LnIkmm4-_Xvgk0Vyq7a-nTkl419-dBnml_jITmJ8PYJGUt1'
#              'NJbNsw4oK-4aEjdj8KoLCXYgblbrOm9z751ihiIgavj8uV9d8N-H5-k'
#              'bUm2gGers9QlY87VXOHs1ICURrXcoBTAB; acPostHint=392409f68'
#              'dfd01e0117d6f32fb129bf4f8ce; Hm_lpvt_2af69bc2b378fb58a'
#              'e04ed2a04257ed1=1752052517',
# }
# response1 = requests.get(url2,headers=headers)
# with open('xifan.html','w',encoding='utf-8') as fg:
#     fg.write(response1.content.decode('utf-8'))


# 【****】 requests中cookie参数的使用（重要：用来保持cookie状态往往是失败访问的原因“cookies参数要传递字典”）
# 现创建cookie字典
# temt = ('__51vcke__KGeHxGUwrAhmlpLN=1443b088-4c58-5f24-a953-7170920f7d97; '
#         '__51vuft__KGeHxGUwrAhmlpLN=1735050026555; fps_accelerat=60; hist'
#         'ory_search=%5B%22muv%26type%3Dpost%22%2C%22%5Cu50ac%5Cu7720%26typ'
#         'e%3Dpost%22%2C%22%5Cu50ac%5Cu7720%5Cu6e38%5Cu620f%26type%3Dpost%22'
#         '%5D; showed_bind_reminder=showed; PHPSESSID=2n281dcnuscletktdbj9fc'
#         '2orl; __51uvsct__KGeHxGUwrAhmlpLN=12; wordpress_logged_in_e6d0fbc33'
#         'a82b3d1717d3a200b36a782=%E6%96%B0%E4%B8%96%E7%BA%AA%7C1753263889%7C'
#         'SMSAtpOzmp2zqbZiiJauVtzf3XrIelMTKjqnl953WEa%7C395e2a8876e69ba4c8e57d'
#         '1997e80008b40abc4621d381ce10e5ab57b7fa3477; wfwaf-authcookie-9f303f6f'
#         '97f8a381b4200ecc98abcbad=35991%7Csubscriber%7Cread%7C4e6435659810d45'
#         '9ff22e260cd0370bbef599590b0cdc96042319fdc9f97cc3a; __vtins__KGeHxGUwr'
#         'AhmlpLN=%7B%22sid%22%3A%20%228526f946-9854-56e1-8934-3c338a9bb3b3%22%2C'
#         '%20%22vd%22%3A%209%2C%20%22stt%22%3A%2033640%2C%20%22dr%22%3A%202%2C%2'
#         '0%22expires%22%3A%201752056109591%2C%20%22ct%22%3A%201752054309591%7D')
# 方法一：
# cookie_list = temt.split("; ")
# Cookie1 = {}
# for i in cookie_list:
#     parts = i.split("=")
#
#     if len(parts) == 2:  # 增加判断，确保有键值对
#         key = parts[0].strip()
#         value = parts[1].strip()
#         Cookie1[key] = value
# print(Cookie1)
#方法二：字典推导式
# headers = {
#     'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#                  "AppleWebKit/537.36 (KHTML, like Gecko) Chr"
#                  "ome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
#     'Referer':'https://www.nekogal.com/',
# }
# url2 = "https://www.nekogal.com/user/balance"
# response1 = requests.get(url2,headers=headers,cookies=Cookie1)
# with open('NEKOGAL.html','w',encoding='utf-8') as fg:
#     fg.write(response1.content.decode('utf-8'))


# 【cookiejar对象的处理】
"""将返回的cookie转换为字典"""
# url = 'http://www.baidu.com'
# reap = requests.get(url) #此时就是一个cookiejar对象
# print(reap.cookies)
# dict_cookie = requests.utils.dict_from_cookiejar(reap.cookies) #次时域名消失，用requests.utils.dict_from_cookiejar（）函数。
# print(dict_cookie)


# 【超时参数timeout的使用】
# url = 'https://twitter.com'
# response1 = requests.get(url,timeout=5)  #设置最大的连接时间


# 【代理proxies的使用用来设置代理ip】
# url2 = 'http://httpbin.org/ip'
# url3 = 'http://www.baidu.com/'
# proxies = {
#     'https':'https://116.208.205.245:17790'
# }
# reap3 = requests.get(url3,proxies=proxies,timeout=4)
# print(reap3.text)


#【requests中的verify参数和CA证书】
#有些网站没用在官方注册过，即（该网站的CA证书没用经过“受信任的根证书颁发机构”的认证）此时令verify=False即可
# url = "https://jwxt.jxsdky.edu.cn:8081/cas/login.action"
# reap = requests.get(url,verify=False)
# print(reap.text)


# 13.requests发送post请求[重点是传递一个data字典类型参数]
'''
思考:哪些地方我们会用到POST请求?
1.登录注册(在web工程师看来POST比GET更安全,url地址上中不会暴露用户的账号密码等信息)
2.需要传输大文本内容的时候(POST请求对数据长度没有要求)所以同样的,我们的爬虫也需要在这两个地方回去模拟浏览器发送post请求
'''
#搜狗翻译案例
# import json
# import requests
# class SouGouTranslate:
#     def __init__(self, word):
#         self.url = "https://fanyi.sogou.com/reventondc/suggV3"
#         self.headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                           'AppleWebKit/537.36 (KHTML, like Gecko) Chr'
#                           'ome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
#             'referer':'https://fanyi.sogou.com/text?',
#             'host':'fanyi.sogou.com'
#         }
#         self.data = {
#             'from':' auto',
#             'to': 'en',
#             'client': 'web',
#             "text": word,
#             "uuid":'10a91ef5-6d6e-40f5-83fa-707bf5495039',
#             "pid": 'sogou-dict-vr',
#             "addSugg":"on",
#         }
#     def post_function(self):
#         reap = requests.post(url=self.url, headers=self.headers, data=self.data)
#         return reap.text
#     def jie(self, data):
#         # 直接用 json.loads 解析字符串
#         dict_data = json.loads(data)
#         print(dict_data)  #经过loads的转化为字典
#         word_list = (dict_data['sugg'][0])
#         word_list1 = list(word_list.items())
#         i = word_list1[1][1]
#         ii = i.split(";")
#         return ii[0]
#     def run(self):
#         result = self.post_function()
#         return self.jie(result)
# if __name__ == "__main__":
#     you_word =input('请输入你要查找的单词: ')
#     sougou = SouGouTranslate(you_word)
#     # 调用 run 后打印结果
#     print(sougou.run())


# 【post数据来源】
'''
2.post数据来源
1.固定值:           抓包比较不变值
2.输入值 :          抓包比较根据自身变化值
3.预设值-静态文件:    需要提前从惊天html中
4.预设值-发请求:     需要对指定地址发送请求
5.在客户端生成的 :   分析js,模拟生成数据
'''

# 【requests模块--session的使用】
'''
session:
之前使用urllib库,是可以使用opener发送多个请求,多个请求,多个请求之间是可以共享cookie的。
那么如果使用requests,也要达到共享cookie的目的,那么可以使用requests库给我们提供的session对象。
注意,这里的session不是web开发中的那个session,这个地方只是一个会话的对象而已。通过使用requests
来实现。示例代码加下:
requests.session的作用：
        自动处理cookie,即下一次请求会带上前一次的cookie
requests.session的应用场景：
        动处理连续的多次请求过程中产生的cookie
'''
#使用session自动登录A站
# url1 = "https://id.app.acfun.cn/rest/web/login/signin"   #登录界面
# url12 = "https://www.acfun.cn"         #首页
# url2 = 'https://www.acfun.cn/member/'  #个人主页
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                  'AppleWebKit/537.36 (KHTML, like Gecko) '
#                  'Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
#     'Origin':'https://www.acfun.cn',
#     'Referer':'https://www.acfun.cn/'
# }
# data = {
#     "username":'18379309798',
#     "password":'A1901420817',
#     "key":'',
#     "captcha":''
# }
# #登录
# session = requests.session()        #实例化session对象
# session.post(url=url1,headers=headers,data=data)
#
# headers1 = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                  'AppleWebKit/537.36 (KHTML, like Gecko) '
#                  'Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
#     'Referer':'https://www.acfun.cn/',
# }
# reap = session.get(url=url2,headers=headers1)
# with open("A漫站网.html",'w',encoding='utf-8') as fg:
#     fg.write(reap.content.decode('utf-8'))


"""
处理不信任的SSL证书:
对于那些已经被信任的SSL整数的网站,比如https://www.baidu.com/,那么使用requests直接就可以正常的返回响应。示例代码
如下:
resp = requests.get("http://www.12306.cn/mornhweb/',verify=False) #添加一个verify参数即可
print(resp.content.decode('utf-8'))
"""