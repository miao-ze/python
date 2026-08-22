import re
import struct


# cafe = bytearray('cafe',encoding='utf-8')
# print(cafe[-1:])



# with open('..\\爬虫\\资料文件\\1.webp','rb') as f:
#     img = memoryview(f.read())
#
#
#
# head = img[:12]
# data = struct.unpack('<4sl4s',head)
# print(data)
# del img
# del head



# name = '中国'
# data = name.encode('utf-16BE')
# print(data)
# print(list(data))


# from unicodedata import normalize
#
# a1 = "中国e\u0301"
# a2 = "中国"
#
# print(a1)
# print(normalize('NFD',a1))


# import locale
# locale.setlocale(locale.LC_COLLATE, '')
# nation = ['中国','美国','法国','日本']
# nation.sort(key=locale.strxfrm)
# print(nation)


import pyuca
coll = pyuca.Collator()
nation = ['中国','美国','法国','日本']
nation.sort(key=coll.sort_key)
print(nation)



str1 = '爱上放大了法尔中国啊多发点'
str2 = b'\xssdfa23\xcsadf3'
data = re.compile(rb'\s')
print(re.findall(data,str2))
