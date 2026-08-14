# （一）应用烤地瓜

'''
需求主线：
1.被烤的的时间和对应的地瓜状态
0-3分钟：生的
3-5分钟：半生
5-8分钟：熟了
超过8分钟：烤糊了
2.添加调料：
用户可以安自己的意愿添加调料
'''



"""
步骤分析

需求涉及一个事物：地瓜。故案例涉及一个类：地瓜类
1.定义类
1.1地瓜的属性
    被烤的时间
    地瓜的状态
    添加的调料
1.2地瓜的方法
    被烤
        用户根据自己的意愿设定每次烤地瓜的时间
        判断地瓜被烤的总时间是在哪个区间，修改地瓜的状态
    添加调料
        用户根据意愿设定添加的调料
        将用户添加的调料存储
1.3显示对象

"""



# 1.定义类 （初始化属性，被烤和添加调料的方法，显示对象的信息__str_)
class SweetPotato():
    #进行初始化属性设置 函数：__init__()
    def __init__(self): #魔法方法会自动调用
        #被烤的时间
        self.cool_time = 0
        #烤的状态
        self.cool_state = '生的'
        #调料列表
        self.condiments = []
    def cool(self,time):
        """烤地瓜的方法"""
        #1.先计算地瓜整体的烤过时间
        self.cool_time += time
        #2.用烤的时间来判断烤的状态
        if 0 <= self.cool_time < 3:
            self.cool_state = '生的'
        elif  3 <= self.cool_time < 5:
            self.cool_state = '半生不熟'
        elif 5 <= self.cool_time < 8:
            self.cool_state = '熟了'
        elif self.cool_time >= 8:
            self.cool_state = '烤糊了'
    #用户自定义添加调料
    def add_condiments(self,condiment):
        self.condiments.append(condiment)
    def __str__(self):  #会自动调用
        return f'这个地瓜的被烤时间是：{self.cool_time},状态是：{self.cool_state}，调料有{self.condiments}'

# 2.创建对象
digua1 = SweetPotato()
print(digua1)   #调用了魔法方法（因为会自动调用）

digua1.cool(2)
print(digua1)

digua1.cool(2)
print(digua1)

digua1.cool(2)
print(digua1)

digua1.add_condiments('辣椒')
print(digua1)

digua1.add_condiments('青菜')
print(digua1)





# （二）搬家具
#需求：将小于房子剩余面积的家具摆放到房子中
"""需求涉及两个事物：房子 和 家具 ，所以案例涉及两个类（要定义两个类）"""

'''
定义类
房子类
    实例属性
        房子地理位置
        房子占地面积
        房子剩余面积
        房子内家具列表
    实例方法
        容纳家具
    显示房屋信息
家具类
    家具名称
    家具占地面积
'''

# 定义家具
class Furniture():
    def __init__(self,name,area):
        self.name = name
        self.area = area


#定义房子类
class Home:
    def __init__(self,address,area):
        # 房子地理位置
        self.address = address
        # 房子占地面积
        self.area = area
        # 房子剩余面积
        self.free_area = area
        # 房子内家具列表
        self.furniture = []
    def __str__(self):
        return f"房子的位置位于：{self.address}，房子的占地面积是：{self.area}，剩余面积：{self.free_area}，家具有：{self.furniture}"

    def add_furniture(self,item):
        '''容纳家具'''
        #如果家具占地面积 <=房子剩余面积。可以搬入
        if item.area <= self.free_area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print('用户家具太大，剩余面积不足，无法容纳')


# 家具
bed = Furniture('双人床',10)
sofe = Furniture('沙发',6)
ball = Furniture('球产',2000)
# 房子
jia1 = Home('北京',1000)
print(jia1)

#开搬
jia1.add_furniture(bed)
print(jia1)

jia1.add_furniture(ball)
print(jia1)





















