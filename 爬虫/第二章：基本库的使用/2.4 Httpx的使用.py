import http.cookiejar
import json

import httpx
import requests


url_bi = 'https://www.bilibili.com/'
url_lz = 'https://lzacg.cc/'
url_bu = 'https://www.baidu.com'
url_mv = 'https://ssr1.scrape.center/'
url_hp_p = 'https://www.httpbin.org/post'
url_hp_g = 'https://www.httpbin.org/get'


# client = httpx.Client(http2=True)
# res = client.get('https://spa16.scrape.center/',)
# print(res.status_code)
# print(res.text)
# print(json.dumps(res.text))


# header = {
#     'User_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
# }
# client = httpx.Client(http2=True)
# res = client.get(url_hp_g,headers=header)
# print(res.text)
# print(res.http_version)



cookies = ('buvid3=C76E707D-90B6-0CDA-6C66-CE193632136810978infoc; '
           'b_nut=1783418110; _uuid=541010FE95-83FB-E67E-7E2E-78C49310826AA96227i'
           'nfoc; buvid_fp=26dc4f09984007bd2a8462ffa67aec61; buvid4=4A44B0FF-D513-E0E1-B9FD'
           '-C5D9FA35850712315-026070717-psgrJu9X6lp70LOMTNDknh8BQnLsoxmTUbxZxDozEJlphr79K'
           'p9FbutMNnieT/q9; rpdid=0zbfAHNVpW|c8yfN90|1HHC|3w1WH2wt; theme-tip-show=SHOWED; CURRE'
           'NT_QUALITY=80; theme-avatar-tip-show=SHOWED; DedeUserID=3546718589160056; DedeUserID__ckMd5'
           '=b123c67857be9e2f; SESSDATA=228b0df5%2C1802394577%2Cf676d%2A82CjBP4sQA7MdN3GyAIGssPIOqs4QSqk'
           'eJt6dqqXZv3OZx9oQiUPOwLhQZVqJpKx9wSEsSVlhkNlF6OTlmTHFoT2xXTXNOTGhRSHVQR2hoakNoS0x6YUhsYlVjTG1'
           'fdWp1c0RKZkR5UFRHdGxYd1pqRVM0TEVkT0ZFWU54dm56N3dqajJvbG9RT0h3IIEC; bili_jct=6cbc12c8d4c45f5a2b'
           '7a0060d9664b77; sid=4otm9hpl; bp_t_offset_3546718589160056=1236968551391166464; bili_ticket=eyJh'
           'bGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3ODcxMjQzMTAsImlhdCI6MTc4Njg2NTA1MCwi'
           'cGx0IjotMX0.eBgXep56HAuoxc_kQ5rVKcq9A5cD16--yZ9bDtEWm_g; bili_ticket_expires=1787124250; PVID=1; LIV'
           'E_BUVID=AUTO3917868651115656; CURRENT_FNVAL=4048; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; b'
           'mg_af_sc={"none":{"on":1,"def":"i1.hdslb.com"},"sgp":{"on":1,"def":"i1-sgp.hdslb.com"}}; home_feed_colu'
           'mn=4; browser_resolution=800-922; b_lsid=6DB63987_1A01204E377')

jia = {}
for cookie in cookies.split(';'):
    key,value = cookie.split('=')
    jia[key] = value

header = {
    'User_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
    'Cookies':cookies
}
with httpx.Client(http2=True,headers=header,cookies=jia) as client:
    res = client.get(url_bi)
    print(res.text)