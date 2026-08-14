
"""

1.HTTP协议
协议:就是两个计算机之间为了能够流畅的进行沟通而设置的一个君子协定.常见的协议有TCP/IP, SOAP协议, HTTP协议, SMTP协议等等....
HTTP协议, Hyper Text Transfer Protocol (超文本传输协议) 的缩写,是用于从万维网 (WWW:World Wide Web ) 服务器传输
超文本到本地浏览器的传送协议. 直白点儿, 就是浏览器和服务器之间的数据交互遵守的就是HTTP协议.
HTTP协议把一条消息分为三大块内容. 无论是请求还是响应都是三块内容

请求:
1 请求行 -> 请求方式(get/post) 请求url地址 协议
2 请求头 -> 放一些服务器要使用的附加信息
3-----------------------------
4 请求体 -> 一般放一些请求参数

在Http协议中,定义了八种请求方法。这里介绍两种常用的请求方法,分别是get请求和post请求
1.get请求:一般情况下,只从服务器获取数据下来,并不会对服务器资原产生任何影响的时候会使用get请求。
2.post请求:向服务器发送数据(登录)、上传文件等,会对服务器资源产生影响的时候会使用post请求。
以上是在网站开发中常用的两种方法。并且一般情况下都会道循使用的原则。但是有的网站和服务器为了做反爬虫机制,也经常会不
按常理出牌,有可能一个应该使用get方法的请求就一定要改成post请求,这个要视情况而定。
响应:

1 状态行 -> 协议 状态码
2 响应头 -> 放一些客户端要使用的一些附加信息
3-----------------------------
4 响应体 -> 服务器返回的真正客户端要用的内容(HTML, json)等


2.http以及https的概念和区别：
HTTPS比HTTP更安全,但是性能更低
HTTP:超文本传输协议,默认端口号是80
。超文本:是指超过文本,不仅限于文本;还包括图片、音频、视频等文件
。传输协议:是指使用共用约定的固定格式来传递转换成字符串的超文本内容
HTTPS:HTTP+SSL(安全套接字层),即带有安全套接字层的起本文传输协,默认端口号:443
。SSL对传输的内容(超文本,也就是请求体或响应体)进行加密
可以打开浏览器访问一个url,右键检查,点击network,点选一个url,查看http协议的形式


3.一些重要的请求头信息：；
http请求的形式如上图所示,爬虫特别关注以下几个请求头字段
Content-Type
Host            ：(主机和端口号)
Connection      ：(链接类型)
Upgrade-Insecure-Requests(升级为HTTPS请求)
*重要 User-Agent      ：(用户代理，提供系统信息，和浏览器信息)
*重要 Referer         ：(页面跳转处，防盗链)
*重要 Cookie          ：(保持转态)Cookie:http协议是无状态的。也就是同一个人发送了两次请求,服务为器没有能力知道这两个请求是否来自同一个人。因此这
                            时候就用cookie来做标识。一般如果想要做登录后才能访问的网站,那么就需要发送cookie信息了。
Authorization： ：(用于表示HTTP协议中需要认证资源的认证信息,如前边web课程中用于jwt认证)

一、常见请求头

分类      	头字段	    说明	                示例
内容协商 :Accept	客户端接受的响应内容类型	application/json, text/html
        Accept-Encoding	支持的压缩算法	gzip, deflate, br
        Accept-Language	客户端偏好的语言	zh-CN, en-US
缓存控制	：Cache-Control	缓存策略	no-cache, max-age=3600
身份验证	：Authorization	携带认证凭证	Bearer xxxxxxx (JWT 令牌)
        Cookie	客户端存储的会话信息	session_id=abc123
请求元信息：	Content-Type	请求体的 MIME 类型	application/json
            Host	请求的目标主机和端口	api.example.com:443
            User-Agent	客户端信息	Mozilla/5.0 (Windows NT 10.0)
连接管理	：Connection	控制连接状态（HTTP/1.1）	keep-alive (保持长连接)
隐私控制	：DNT	客户端请求不追踪用户行为	DNT: 1 (不允许追踪)

重要的请求头为常用请求头,在服务器被用来进行爬虫识别的频率率最高,相较于其余的请求头
更为重要,但是这里需要注意的是并不意味这其余的不重要,因为为有的网站的运维或者开发人
员可能剑走偏锋,会使用一些比较不常见的请求头来进行爬虫的甄别


4.反应头信息：
二、常见响应头
分类          头字段                              说明                             示例
内容描述    Content-Type                         响应体的 MIME类型            application/json; charset=UTF-8
           Content-Encoding                    响应体的压缩算法                 gzip
缓存控制    Cache-Control                        服务器指定的缓存策略              public, max-age=3600
安全策略    Content-Security-Policy (CSP)        防止 XSS 攻击，限制资源加载来源     default-src 'self'; script-src 'unsafe-inline'
            Strict-Transport-Security (HSTS)   强制 HTTPS 连接                  max-age=31536000; includeSubDomains
            X-Content-Type-Options             禁止 MIME 类型嗅探                   nosniff
            Permissions-Policy                 限制浏览器 API 使用（如摄像头、麦克风） geolocation=(), microphone=()
重定向与会话  Location                             重定向目标 URL                   https://example.com/new-path
            Set-Cookie                           服务器设置的 Cookie               session_id=abc123; Path=/; HttpOnly
服务器信息 Server 服务器软件信息 Apache/2.4.57


5.状态码
所有的状态码都不可信,一切以是否从抓包得到的响应中获取到到数据为准
network中抓包得到的源码才是判断依据,elements中的源码是渲染之后
三、常见状态码
分类	状态码	说明	示例场景
1xx 信息性	100	客户端可继续发送请求体（常用于分块上传）	上传大文件时，服务器接收请求头后返回 100，客户端继续发送文件内容
101	协议切换成功（如升级到 WebSocket）	客户端请求Upgrade: websocket，服务器返回 101 并切换协议
2xx 成功	200	请求成功，资源正常返回	GET 请求获取数据成功
201	资源创建成功（如 POST 请求）	提交表单创建新用户
204	请求成功，但无返回内容	DELETE 请求删除资源成功
3xx 重定向	301	资源永久移动，需更新 URL	网站域名变更，旧 URL 永久重定向到新域名
304	资源未修改，客户端可使用缓存数据	浏览器缓存图片，再次请求时服务器返回 304
4xx 客户端错误	400	请求语法错误或参数无效	发送无效 JSON 格式数据
401	未提供或认证失败，需重新登录	访问需要登录的 API 时未携带 Token
403	权限不足，禁止访问资源	普通用户尝试访问管理员接口
5xx 服务器错误	500	服务器内部错误（如代码异常）	后端代码抛出未捕获异常
502	上游服务器返回无效响应（如代理错误）	Nginx 连接的后端服务崩溃
503	服务器过载或维护中	高并发时服务器暂时无法处理请求


四、安全与优化补充
分类	        头字段	            说明	            示例
安全头	X-Frame-Options	    防止点击劫持	        DENY（禁止在 iframe 中加载）
        Referrer-Policy	    控制 Referer 头的发送	no-referrer（不发送来源 URL）
缓存优化	ETag	            资源的唯一标识，用于缓存验证	"d591be95c5fdfd6b20da5d41e965f6f457286f81"
        If-None-Match	    与ETag 配合，验证资源是否未修改	If-None-Match:



http请求的全过程
1.浏览器在拿到域名对应的ip后,先向地址栏中的url发起请求,并获取响应
2.在返回的响应内容(html)中,会带有css、js、图片等url地址,以及ajax代码,浏览器按照响
  应内容中的顺序依次发送其他的请求,并获取相应的响应
3.浏览器每获取一个响应就对展示出的结果进行添加(加载),js,css等内容会修改页面的内
  容,js也可以重新发送请求,获取响应
4.从获取第一个响应并在浏览器中展示,直到最终获取全部响应,并在展示的结果中添加内容或修
  改---这个过程叫做浏览器的渲染

注意:
但是在爬虫中,爬虫只会请求url地址,对应的拿到url地址对应应的响应(该响应的内容可以是html,css,js,图片等)
浏览器渲染出来的页面和爬虫请求的页面很多时候并不一样,是因为爬虫不具备渲染的能力(当然后续课程中我们会借助其它工具或包来帮助爬虫对响应内容进行(Fr)
浏览器最终展示的结果是由多个url地址分别发送的多次请求对应的多次响应共同渲染的结果所以在爬虫中,
需要以发送请求的一个url地址对应的响应为X准来进行数据的提取


骨骼文件：
html静态文件
肌肉文件：
js/ajax请求
皮肤：
css/font/图片

（抓包过程：
        根据发送到请求的流程分别在骨骼/肌肉/皮肤响应中查找数据）
"""