#导入模块的写法“3种基本的”
"""
1.import 模块名
2.from 模块名 import 功能名
3.from 模块名 import *
"""
#调用功能

#一。需求：math模块下的sqrt（）

#方法一：1.import 模块名                                功能调用（模块名.功能名）
# import math
# print(math.sqrt(9))

#方法二：2.from 模块名 import 功能名(功能1 功能2 功能3)     功能调用（不需要书写模块名）
# from math import sqrt
# print(sqrt(8))

#方法三：3.from 模块名 import *    （导入这个模块下的所有代码“所用功能”）
# from math import *
# print(sqrt(4))

# 二。as定义别名
"""
模块定义别名
import 模块名 as 别名

功能定义别名
from 模块名 import as 别名

#设置了别名后，就只能用别名调用
"""
#需求：运行后暂停2秒打印hello
# 1.
# import time as cc
# cc.sleep(2)
# print('cello')

# 2.
# from time import sleep as dd
# dd(2)
# print('sd')

# 三。制作模块
#在python中，每个python文件都可以作为一个模块，模块的名字就是文件的名字，也就是说自定义模块名必需要符合标识符命名的规则
# 1.定义模块    （新建一个python文件，并命名my_module1,"要满足命名规则"）
# 2.进行测试    (if __name__ == "__main__"）
# 3.调用模块

# from my_module1 import test1 as cc
#   进行调用
# cc(1,3)
#
# 四。模块定为顺序
'''当导入一个模块时，python解释器对模块位置的搜索顺序是：
1.当前目录
2.如果不在当前目录，python则搜索在shell变量PYTHONPATH下的每一个目录       (PYTHONPATH)
3，如果都找不到，python会察看默认路径，UNIX操作系统下，默认路径一般为/usr/local/lib/python/
（由近及远）
'''
#注意；    1.自己的文件名不要和已有的模块名重复，否则导致模块功能无法使用
#         2.使用from 模块名import 功能的时候如果功能名重复，调用的是最后定义或导入的功能

# 拓展--（名字重复的严重性）

# 五 ：__all__   列表(只能导入all列表中含有的功能)
# from my_midule2 import *
# textA()         #在all列表中所以可以使用功能
# textB()         #不在all列表中所以不可以使用

 # 六。包
"""包就是将有联系的模块组织在一起，即放到同一个文件夹下，并且在这个文件夹创建一个名字为__init__.py文件，那么这个文件夹就称为包"""

# 六.1 制作包
# 1.新建包mypackage
# 2.新建包内的模块：my_module1和my_module2
# 3.在模块下写入代码（即功能）


# 七，导入包
'''
方法一：    
import 包名.模块名
包名.模块名.目标

方法二：#（注意：必须在__init__.py文件中添加__all__ = [],控制允许导入的模块列表）
from 包名 import *
模块名.目标
'''
# 1,/
from mypackage.my_moduleA import info_print1 as bb

bb()


# 2./
# from mypackage import *
# my_moduleB.info_print2()













