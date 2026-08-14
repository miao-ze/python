
# 正则表达式匹配单个字符规则：
# 点（.）：匹配除换行符外的任意一个字符。
# 中括号（[]）：匹配列举中的任意一个字符，未列举的不匹配，列举时不能用逗号，否则逗号也会被匹配。
# 反斜杠 d（\d）：匹配 0 - 9 中的一个数字，等价于 [0 - 9]。
# 反斜杠大 D（\D）：匹配非数字字符，与 \ d 取反。
# 反斜杠小 s（\s）：匹配空白字符，包括空格和 Tab 键。
# 反斜杠大 S（\S）：匹配非空白字符，与 \ s 取反。
# 反斜杠小 w（\w）：匹配字母、数字、下划线和汉字。
# 反斜杠大 W（\W）：匹配非字母、非数字、非下划线、非汉字的字符。

import re

# 1. . 匹配任意1个字符（除了\n即换行符）
match_obj = re.match("t.w",'tqw')
if match_obj:
    result = match_obj.group()
    print(result)
else:
    # 匹配失败match_obj是一个noll
    print('匹配失败')

# 2. [] 匹配列表中的一个数据
match_obj = re.match("石头门[12]",'石头门2')
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print('匹配失败')

#匹配0到9之间的数字[0-9] = [0123456789]
match_obj = re.match("[0-9]",'2')
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print('匹配失败')

# 3. \d ==> [0-9] 匹配0到9中的一个数字
match_obj = re.match(r"\d","3")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print('匹配失败')

# 4. \D 匹配任意一个非数字
match_obj = re.match(r"\D","S")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print('匹配失败')

# 5. \s 匹配空白字符 如空格和tab键
match_obj = re.match(r"石头门\s[12]",'石头门\t2')
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print('匹配失败')

# 5. \S 匹配非空白字符 如空格和tab键如石头{石头门后不可为空格}
match_obj = re.match(r"石头门\S",'石头门2')
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print('匹配失败')

# 6. \w 匹配数字、字母、下划线、汉字
match_obj = re.match(r"石头\w门",'石头只门')
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print('匹配失败')

# 6. \W 匹配非数字、字母、下划线、汉字
match_obj = re.match(r"石头\W门",'石头&门')
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print('匹配失败')






























