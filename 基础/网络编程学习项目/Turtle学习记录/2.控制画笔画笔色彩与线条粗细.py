import turtle,random




# 控制画笔画笔色彩与线条粗细（案例1）

'''
pen = turtle.Pen()
pen.speed(10)
#创建画笔的初始粗细度 控制画笔画笔色彩与线条粗细（案例3）
size_pen = 1.0

#创建颜色列表
color_list = ['red','orange','yellow','green','blue','violet','cyan','purple']

for i in range(1,41):
    size_pen += i * 0.05
    pen.pensize(size_pen)
    pen.color(color_list[i % 8])
    pen.forward(2 + i * 5)  #令前进步数一直在变化
    pen.right(45)
turtle.done()
'''

# 控制画笔画笔色彩与线条粗细（案例2）

'''
pen = turtle.Pen()

#修改画笔的宽度
pen.pensize(4)
pen.speed(0)

for i in range(36):
    color1 = 1.0
    color2 = color1 / 4
    color1 -= color2   #使每次变化b的值
    pen.color(0.3, 1,color1)
    for j in range(3):
        pen.forward(100)
        pen.left(90)

    #绘制第四条边
    pen.forward(100)
    pen.left(100)

turtle.done()
'''
# 控制画笔画笔色彩与线条粗细（案例3）

pen = turtle.Pen()
pen.pensize(1)
pen.speed(0)
pen.color('blue')
for i in range(0,301,10):
    #1.抬起画笔
    pen.penup()
    #2.设置绘图的起始坐标
    pen.setposition(i,0)
    pen.forward(100)
    #3.放下画笔
    pen.pendown()
    #2.设置绘图的终点坐标
    pen.setposition(0,300-i)

    pen.pendown()

turtle.done()

# 控制画笔画笔色彩与线条粗细（案例4）

#
# pen = turtle.Pen()
# pen.pensize(1)
# pen.speed(0)
#
# #创建颜色列表
# color_list = ['red','orange','yellow','green','blue','violet','cyan','purple']
# for i in range(0,301,10):
#     pen.color(random.choice(color_list))
#     #设置坐标
#     pen.setposition(i,0)
#     pen.setposition(0,300-i)
#     pen.setposition(-i,0)
#     pen.setposition(0,i-300)
#     pen.setposition(i,0)
#
# turtle.done()









