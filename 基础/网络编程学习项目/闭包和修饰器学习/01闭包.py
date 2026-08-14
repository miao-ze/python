
# 闭包的作用：为了保存外部函数的变量
'''
创建闭包的条件：
1.函数嵌套
2.内部函数使用了外部函数的变量
3.外部函数返回了内部函数
'''
# 1.创建嵌套函数
def out_test():
    num = 1
    def inner_test(num2):
        # 2. 内部函数使用了外部函数的变量
        result = num + num2
        print(result)
    # 3. 外部函数返回内部函数 注意：不要加括号，加括号的结果是返回内部函数的执行结果，而非内部函数本身
    return inner_test
# 获取闭包对象
# 这里的new_result就是闭包: new_result = inner_test
new_result = out_test()
# 执行闭包
new_result(3)