
def out():
    num1 =10
    def inner():
        # num1 = 20    # 本意是修改外部变量，但实际则是创建了一个局部变量
        nonlocal num1  # 需使用nonlocal关键字进行声明
        num1 = 20
        result = num1 + 15
        return result
    inner()
    print("修改后的值：",num1)
    return inner

# 创建闭包啊对象
new_object = out()
# 执行对象
print(new_object())