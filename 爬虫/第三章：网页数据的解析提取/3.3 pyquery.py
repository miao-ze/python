from pyquery import PyQuery as pq
import requests



# with open('..\\资料文件\\lzacg_detail.html','r',encoding='utf-8') as f:
#     data = f.read()
# doc = pq(data)
# result = doc('.theme-box .wp-posts-content')
# print(list(result.find('p').siblings('p').items()))
# print(result.attr('class'))



doc = pq(url='https://lzacg.cc/10637')
data = doc('p:last-child')
print(data)


























