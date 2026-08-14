
"""认识海龟"""

# #1.导入海龟绘图模块 {导入turtle库}
# import turtle, time
# #2.获取画笔  并用一个变量去接收画笔：{Pen}方法
# t = turtle.Pen()
# # 3. 设置海龟的形状： {shape方法}
# # 形状1
# t.shape('turtle')
# # 形状2
# t.shape('circle')
# # 输出并查看海龟的所用形状  打印出后显示有7种形状 ： (['arrow', 'blank', 'circle', 'classic', 'square', 'triangle', 'turtle'])
# print(t.screen.getshapes()) # 注意要用print输出
# # 隐藏海龟（用sleep方法可以更好体现)
# time.sleep(1)
# t.hideturtle()
# # 显示海龟 (用sleep方法可以更好体现)
# time.sleep(1)
# t.showturtle()
# #4. 保持屏幕的显示：{done}方法
# turtle.done()
#

'''动起来'''
# import turtle,time
# pen = turtle.Pen()      #创建画笔
# pen.shape('turtle')     #设置形状
# #动起来：让海龟前进100个像数  {forword方法}
# pen.forward(100)
# time.sleep(1.5)  #加入时间好区分
# #让海龟向后前进120个像数
# pen.forward(-120)
# #让海龟留下印记（盖章）：     {stamp方法}
# pen.stamp()
# #让海龟回家即回到原点：       {home方法}
# time.sleep(1.5)  #加入时间好区分
# pen.home()
# turtle.done()           #保持屏幕


"""调转方向"""
# import turtle
# pen = turtle.Pen()
# pen.shape('turtle')
# # 往0’度方向前进
# pen.forward(100)
# pen.stamp()
# pen.home()
# # 调转到15‘方向 :{setheading方法}
# pen.setheading(15)
# pen.forward(100)
# pen.stamp()
# pen.home()
# turtle.done()
#
#
# '''用循坏操作来调转方向'''
# import turtle
# pen = turtle.Pen()
# #用循环来控制海龟的方向
# for i in range(0,361,15):
#     pen.shape('arrow')
#     pen.setheading(i)
#     pen.forward(100)
#     pen.stamp()
#     pen.home()
# turtle.done()


'''简单的绘图练习'''
import turtle
# 绘制三角形（绘制正方形时：是只需改为循环四次，旋转角改为90度即可）(绘制五角形时：是只需改为循环5次，旋转角改为144度即可)
pen = turtle.Pen()
#设置画笔的颜色
pen.color("red")
#设置海龟的速度
pen.speed(2)
for i in range(5):
    pen.forward(100)
    pen.right(144) #(也可改为逆时针旋转)
    pen.stamp()
turtle.done()