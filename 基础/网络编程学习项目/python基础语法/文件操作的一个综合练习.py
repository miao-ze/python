with open('data.csv', 'r', encoding='utf-8') as file1:
    '''创建第一个列表用来把记事本中的字符串改为列表'''
    list1 = []
    lines2 = file1.read()  # 读取记事本中所有的内容
    fen_lines2 = lines2.split('\n')  # 通过分割函数spilt以换行符'\n',将记事本的内容以行为单位转换为列表（split函数返回的是列表）
    for mun in range(0, len(fen_lines2)):
        list1.append(fen_lines2[mun].split(','))  # 将每一行以逗号为标志分为列表，所以添加到list1后就构成了二维列表

list1[0].append('总分')

# 计算每个学生的分数
'''创建第二个列表用来将‘总分’，和‘成绩’添加到列表里去。'''
new_list = []
new_list.append(list1[0])
for x in list1[1:]:  # x代表的是每位学生的成绩信息（数据类型为列表）
    result1 = sum(list(map(int, x[1:])))  # 注意map函数可以转换列表中元素的数据类型（后面的list是一定要有的）
    x.append(str(result1))
    new_list.append(x)

# 分出开头
new_list_title = new_list[0]

# 分出成绩部分
new_list_grade = new_list[1:]

# 按成绩进行排序
new_list_grade.sort(key=lambda x: x[-1], reverse=True)

"""创建第三个列表用来对学生的成绩进行排序"""
new_list_rank = []
new_list_rank.append(new_list_title)
new_list_rank.append(new_list_grade)

# print(new_list_rank)
# # 开始进行写入操作
# with open('8.2 scoreSort.csv', 'w+', encoding='utf-8') as file2:
#     # 因为不可直接添加列表所以要进行list变为str的操作
#
#     str_title = ','.join(new_list_rank[0])  # 将第一行以逗号为标志进行连接（join函数连接后为字符串）
#     file2.write(str_title + '\n')  # 写入转换完成后的字符串（注意要加入换行符\n）
#     for a in new_list_rank[1]:
#         str_grade = ','.join(a)
#         file2.write(str_grade + '\n')
#
# with open('8.2 scoreSort.csv', 'r', encoding='utf-8') as file2:
#     print(file2.read())
