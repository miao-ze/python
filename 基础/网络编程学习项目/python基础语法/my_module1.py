#需求：一个函数(即设置功能)，完成任意两个数字的加减
def test1(a,b):
    print(a+b)

#进行测试: if __name__ == "__main__"
print(__name__)
#只在当前文件中调用该函数，其他导入的文件内不符合该条件，则不执行该函数的调用
if __name__ == "__main__":  #__name__是系统变量，是模块的标识符，值是：如果是自身模块值是__main__,否则是当前的模块的名字
    test1(1,2)


# from matplotlib import pyplot as plt
# x = range(2,26,2)
# y = [15,13,14.5,17,20,26,25,26,22,18,15]
# plt.plot(y)
# plt.show()







