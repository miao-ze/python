

'''绘制圆与圆弧知识点'''
import turtle
pen = turtle.Pen()
pen.color('blue')
pen.speed(0)

# #绘制圆时，如果只传递一个参数，那么该参数代表的是圆的半径
# pen.circle(50,90,)
#
# turtle.done()




'''练习1(绘制4个圆和绘制圆弧)'''
# import turtle
# pen = turtle.Pen()
# pen.color('blue')
# pen.speed(0)
#抬起画笔
# pen.penup()
# pen.setheading(180)
# pen.forward(150)
# pen.setheading(0)
# #放下画笔
# pen.pendown()
#绘制圆
# pen.circle(50)
# pen.circle(-50)
# pen.forward(100)
# pen.circle(50)
# pen.circle(-50)
# pen.forward(100)
# pen.circle(50)
# pen.circle(-50)

#运用循环实现圆弧的绘制
#
# for i in range(10,101,3):
#       pen.penup()           #起笔
#       #绘制圆弧的起点
#       pen.setposition(150,-100)
#       pen.setheading(0)
#       pen.pendown()         #落笔
#       #开始绘制
#       pen.circle(i,90 + i * 2)
#
#
# turtle.done()


'''练习2'''

# for r in range(0,361,10):
#     pen.setheading(r)
#     pen.circle(100)
#
#
# turtle.done()

'''练习3'''

# pen.penup()
# pen.setheading(180)
# pen.forward(100)
# pen.setheading(0)
#
# for i in range(3,13):
#     pen.pendown()
#     pen.circle(30,steps=i)
#     pen.penup()
#     pen.forward(30)
#
#
# turtle.done()
#























