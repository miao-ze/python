
def out(name):
    def inner(speack):
        print(name + ":" + speack)
    # 可以通过查看id来确认所创建对象的id地址是否一致
    print(id(inner))
    return inner
# 创建闭包对象
tom = out('tom')
jerry = out('jerry')
# 使用闭包进行对话
tom('在吗？打王者不')
jerry('不想玩游戏')