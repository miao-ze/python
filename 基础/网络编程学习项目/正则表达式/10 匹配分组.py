# |          匹配左右任意一个表达式
# (a)(b)       将括号中字符作为一个分组
# \num       引用分组num匹配到的字符串
# (?P<name>) 分组起别名
# (?P=name)  引用别名为name分组匹配到的字符串
import re


# 1. | 匹配左右任意一个表达式
fruit_list = ['apple','banana','orage','pear','peach']
for value in fruit_list:
    match_obj = re.match("banana|pear",value)
    if match_obj:
        result = match_obj.group()
        print("我想吃的水果：",result)
    else:
        print('我不想吃的水果：',value)



# 2.(a)(b)将括号中字符作为一个分组
# 匹配出162、126、qq等邮箱
# “\.” :表示对正则表达式里面进行了转义，变成了一个普通点。 只能匹配.字符
# (192|162|qq) ：表示一个分组，出现一个小括号，就表示一个分组，分组是从1开始
# 如果出现多个小括号，分组的顺序是从左到右
match_obj = re.match(r"([a-zA-Z0-9_]{5,20})@(192|162|qq)\.com","hello@192.com")
if match_obj:
    # 获取整个匹配的数据，如果使用分组，默认为0
    result = match_obj.group(0)
    print(result)
    # 获取分组的数据
    result1 = match_obj.group(2)
    print(result1)
else:
    print('匹配失败')


"""匹配：qq:3014234"""
match_obj = re.match(r"qq:([1-9]\d{4,11})","qq:3014234")
if match_obj:
    # 获取qq号
    result = match_obj.group(1)
    print("qq号为:",result)
else:
    print('匹配失败')

# 3. \num    引用分组num匹配到的字符串(有时用两个反斜杠\\,为了防止转移)
# 匹配html中的双标签 如：<html>hhd</html>
match_obj1 = re.match(r"<([a-zA-Z1-6]+)>.*</\1>","<html>hhd</html>")
if match_obj1:
    result = match_obj1.group()
    print(result)
else:
    print('匹配失败')



# 4.# (?P<name>具体正则表达式)分组起别名   (?P=name)引用别名为name分组匹配到的字符串
match_obj1 = re.match(r"<(?P<html>[a-zA-Z0-9]+)><(?P<p1>[a-zA-Z0-9]+)>.*/<(?P=p1)></(?P=html)>",
                      "<html><h1>https://www.baidu.com/<h1></html>")
if match_obj1:
    result = match_obj1.group()
    print(result)
else:
    print('匹配失败')



