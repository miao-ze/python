'''
可设置窗口标题     scerrn.title()
窗口背景颜色       scerrn.bgcolor()
窗口高度          scerrn.window_hight()
窗口宽度          scerrn.window_weith()
'''

import turtle,random
#定义一个绘制星星的函数
def stars(edges,distance,t_color,x,y):
    pen.penup()
    pen.setposition(x,y)
    pen.pendown()
    angle = 180 - (180 / edges)
    pen.fillcolor(t_color)
    pen.begin_fill()
    for i in range(edges):
        pen.fd(distance)
        pen.right(angle)
    pen.end_fill()
color_list = ['red','orange','yellow','green','blue','violet','cyan','purple']




pen = turtle.Pen()
#设置窗口颜色
pen.screen.bgcolor('blue')
pen.speed(10)
pen.hideturtle()
while True:
    #多变形的变数
    edges1 = random.randint(3,8)
    #产生一个随机颜色
    color1 = random.choice(color_list)
    #对边形的边长
    distance1 = random.randint(5,30)
    #绘制星星的位置
    wei_x = random.randint(-300,300)
    wei_y = random.randint(-300,300)

    stars(edges1,distance1,color1,wei_x,wei_y)


'''实例3.绘制万花筒'''
#定义一个函数，判断绘制的海龟坐标是否在绘制窗口之内
#运行结果：Ture/False
# def is_inside():
#     #定义窗口的宽高
#     width = pen.screen.window_width()      #所得是默认置
#     height = pen.screen.window_height()
#
#
#     #定义绘图边界范围数值
#     right = (-width / 2) + distance
#     left = (width / 2) - distance
#     top = (height / 2) + distance
#     bottom = (-height / 2) - distance
#
#     #获取海龟当前位置
#     x,y = pen.pos()
#     #判断海龟是否越界
#     if right <= x <= left and bottom <= y <= top:
#         return  True
#     else:
#         return False
#
#
# #定义一个海龟移动和函数
# def action():
#     color_list = ['red','orange','yellow','green','blue','violet','cyan','purple']
#     pen.color(random.choice(color_list))
#
#     if is_inside():
#         pen.seth(random.randint(0,360))
#         pen.fd(distance)
#     else:
#         #即绘制坐标超出范围
#         pen.backward(distance)
#
#
#
# pen = turtle.Pen()
# # pen.hideturtle()
# pen.pensize(5)
# pen.screen.bgcolor('black')
# distance = 100
# while True:
#     action()
#










