import re
'''
 ^ 匹配字符串开头
 $ 匹配字符串结尾
'''

# 1.匹配以数字开头
match_obj = re.match(r'^\d.*','13abc')
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print('匹配失败')

# 2.匹配以数字结尾
match_obj = re.match(r'.*\d$','abcd1')
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print('匹配失败')


# 3.匹配以数字开头和结尾
match_obj = re.match(r'^\d.*\d$','3sabcd1')
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print('匹配失败')

"""[^ 指定字符] 表示出指定字符外其他都匹配"""
# [^47]$ 表示在结尾除了47其他都匹配
match_obj = re.match(r'^\d.*[^47]$','3sabcd4')
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print('匹配失败')

# 草稿
match_obj = re.match(r'^\S.*','4msabcd4')
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print('匹配失败')



