import os
import json
import numpy as np
import pandas as pd
import re


# def open_file(file):
#     try:
#         f = open(file,'r',encoding='utf-8')
#         for line in f:
#             print(line.strip())
#     except Exception as e:
#         return e
#     finally:
#         f.close()
#
# # file = '静夜思.txt'
# # open_file(file)
#
#
# def write_file(s,file):
#     with open(file,'a',encoding='utf-8') as f:
#         f.write(s)
#
#
# def writelines_file(s,file):
#     with open(file,'a',encoding='utf-8') as f:
#         f.writelines(s)
#
# def read_file(file):
#     with open(file,mode='r',encoding='utf-8') as f:
#         return f.read()

# file = '静夜思.txt'
# # write_file('独坐敬亭山\n众鸟高飞尽\n古云独自闲\n相看两不厌\n独坐敬亭山\n',file)
# writelines_file(['江雪\n','\t\t千山鸟飞尽\t万径人踪灭\n','\t\t孤舟蓑笠翁\t独钓寒江雪\n'],file)
# result = read_file(file)
# print

# dict1 = {'name':'zp','gender':'男','age':21}
# list1 = [1,2,3,'name',dict1]
# json_object1 = json.dumps(dict1,ensure_ascii=False,indent=4)
# json_object2 = json.dumps(list1,ensure_ascii=False,indent=4)
# print(json_object1)
# print(list1)
# print()
# zhuang1 = json.loads(json_object1)
# print(zhuang1)


# json_dict = '{"name":"秒贼婆","age":21}'
# jie = json.loads(json_dict)
# print(jie)


# 实例8.3 CSV格式与JSON格式的转换
# CSV --> JSON
# def read_document(file):
#     with open(file,'r',encoding='gbk') as f:
#         return [line.strip().split(',') for line in f]
#
# def add_total_score(student_score):
#     end_head = [student_score[0] + ['总分']]
#     tail = student_score[1:]
#     for i in tail:
#         i.append(str(sum(map(int,i[1:]))))
#     return end_head + tail
#
# def crate_json_score(data):
#     date_list = []
#     for i in data[1:]:
#         dict_student = {
#             '姓名':i[0],
#             'C':i[1],
#             'Java':i[2],
#             'Python':i[3],
#             'C#':i[4],
#             '总分':i[5]
#         }
#         pass
#         date_list.append(dict_student)
#     with open('8.3 score.json','w',encoding='utf-8') as f:
#         json_date = json.dump(date_list,fp=f,ensure_ascii=False,indent=4)
#     print(json_date)
#
#
# file = '8.2 score.csv'
# result1 = read_document(file)
# result2 = add_total_score(result1)
# crate_json_score(result2)



# path1 = os.getcwd()
# os.chdir('D:\'')
# path2 = os.getcwd()
# print(path2)


# text = np.genfromtxt('8.5 score.csv',delimiter=',',dtype=None,names=True)
# print(text[['姓名','学号','总分']])


# # 实例8.5 利用numpy库读写数据文件
# result1 = np.genfromtxt('8.5 score.csv',dtype='str',delimiter=',')
# result2 = np.genfromtxt('8.5 score.csv',dtype=None,delimiter=',',names=True)[['姓名','C语言','Java','Python','VB']]
#
# print(result1)
# print(end='\n' * 2)
# print(result2)


# array1 = np.array((1,2,3,4,5,5,))
# array2 = np.array((2,3,4,5,6,7))
# print(array1 + array2)


# result1 = np.genfromtxt('8.5 score.csv',dtype=None,delimiter=',',usecols=(2,3,4,5,6),skip_header=1,filling_values=0)
#
# a = np.amin(result1)
#
# print(a,end='\n' *2)
# print(result1,end='\n' *2)
# print(result1[1],end='\n' *2)


# array1 = np.random.randint(100,size=(3,4))
# print(array1)

# 实例8.6 Numpy数据分析
# result1 = np.loadtxt('8.6 score.csv',str,delimiter=',')
# int_result2 = result1[1:,2:].astype(int)
#
# print(result1,end='\n' * 2)
# print(int_result2,end='\n' * 2)
#
# print('python的平均分：',np.average(int_result2[::,4]))




# data = pd.read_csv('8.5 score.csv',encoding ='gbk')
# print(data)
# print()
# sort_data = data.sort_values('总分',ascending=False)
# print(sort_data.to_string(justify='center'))
# print()
# avg_score1 = round(np.average(sort_data['总分']),2)
# avg_score2 = sort_data['总分'].mean()
# print(avg_score2)

# 实例8.7 Pandas数据分析

# student_data = pd.read_excel('学生成绩表(50人).xlsx')
#
# group_student_by_name = student_data.groupby(student_data['姓名'])
#
# result1 = group_student_by_name['分数'].agg(['mean','max','min'])
# print()
# group_student_by_course = student_data.groupby(['课程名'])
# result2 = group_student_by_course['分数'].agg(['mean','max','min'])
#
# print(result1)
# with pd.ExcelWriter("student_all.xlsx") as writer:
#     result1.to_excel(writer, sheet_name="学生个人统计")
#     result2.to_excel(writer, sheet_name="课程整体统计")
# print("统计结果已全部导出至 student_all.xlsx")

# 本章练习
# （1）
# with open('第八章练习数据\\8.1 IDcode.txt','r') as f1:
#     f1_dict = {}
#     for i in f1:
#         list1 = i.strip().split(',')
#         f1_dict[list1[0]] = list1[1]
#
# local_code = input('地区编码：')
# print(f1_dict[local_code])


# (2)
# f2 = pd.read_csv('第八章练习数据\\8.2 grade.csv',encoding='gbk')
# tuple_list = (
#     ('0','学号'),
#     ('1', '语文'),
#     ('2', '数学'),
#     ('3', '英语'),
# )
# i = input('第几列：')
# for num in tuple_list:
#     if i == num[0]:
#         name = num[1]
#         result = f2.sort_values(name)
#         print(result)
#         break
# else:
#     print('输入错误')


# （3）
# f3 = pd.read_csv('第八章练习数据\\8.3 北京高校名单.csv',encoding='gbk')
# f3_list = f3.values.tolist()
# school_list = []
# for i in f3_list:
#     school_list.append(i[1])
# # 3.1
# school_name1 = input('学校关键字：')
# for name in school_list:
#     if school_name1 in name:
#         print(name)
#
# print()
#
# #3.2
# school_name2 = input('学校：')
# for school in f3_list:
#     if school_name2 in school:
#         school_dict = {
#             '序号':school[0],
#             '学校名称': school[1],
#             '学校标识码': school[2],
#             '主管部门': school[3],
#             '所在地': school[4],
#             '办学层次': school[5],
#             '备注': school[6],
#         }
#         print(school_dict)
#         break
# else:
#     print('不存在')

# （4）
# 读取xlsx文件，强制指定引擎
try:
    f4 = pd.read_excel("第八章练习数据\\8.4 成绩分析综合.xlsx", engine="openpyxl")
    print(f4)
except Exception as e:
    print("读取失败：", e)










