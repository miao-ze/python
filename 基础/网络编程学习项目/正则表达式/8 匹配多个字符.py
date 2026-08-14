import re
# * 匹配前一个字符出现0次或者无限次,即可有可无
# + 匹配前一个字符出现1次或者无限次,即至少有1次
# ? 匹配前一个字符出现1次或者0次,即要么有1次,要么没有
# {m} 匹配前一个字符出现m次
# {m,n} 匹配前一个字符出现从m到n次


#1. * 匹配前一个字符出现0次或者无限次,即可有可无
# 匹配指定字符出现0次或多次 如："to*w" 查询o出现0次或多次
match_obj = re.match("to*w","toooow")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print('匹配失败')

# 匹配任意多个字符
match_obj = re.match("t.*w","to沙发上ow")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print('匹配失败')

#2. + 匹配前一个字符出现1次或者无限次,即至少有1次
match_obj = re.match("t.+w","tow")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print('匹配失败')

#3. ? 匹配前一个字符出现1次或者0次,即要么有1次,要么没有
match_obj = re.match("https?","http")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print('匹配失败')

#4. {m} 匹配前一个字符必需出现m次
match_obj = re.match("ht{2}p","http")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print('匹配失败')

# {m,n} 匹配前一个字符可以出现m次到n次,当n不指定是，表示无限次
match_obj = re.match(r"ht{1,3}p","htp")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print('匹配失败')
