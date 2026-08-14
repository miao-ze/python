# 先导包
import re

# 使用match方法进行匹配操作：match从头进行匹配字符串数据
'''
1.pattern:指要查找查询到数据 ---> 以后用正则表达式代替
2.string：指要进行查找的字符串
3.返回的是一个匹配对象
'''
match_obj = re.match("hel","hello")
# 获取配备结果：group
result = match_obj.group()
print(result)
