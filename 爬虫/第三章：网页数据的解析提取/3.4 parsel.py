import parsel
import requests



with open('..\\资料文件\\lzacg_detail.html','r',encoding='utf-8') as f:
    data = f.read()
# data1 = requests.get('https://lzacg.cc/6485')
# data = data1.text
items = parsel.Selector(data)
# print(items.css('p'))
data2 = items.css('.theme-box.wp-posts-content')
data3 = data2.xpath('//p/text()').getall()
str1 = ''
print(data3)
# while (flag := True):
#     for i in data3:
#         if '解压' in i:
#             flag = False
#         else:
#             str1 += i.strip()
# print(str1)















