
def make_div(func):
    def inner():
        result = "<div>" + func() + "</div>"
        return result
    return inner


def make_p(func):
    def inner():
        result = "<p>" + func() + "</p>"
        return result
    return inner

'''
实际上的 是comment = make_div(@make_p(comment)) 多个装饰器的执行顺序是，先执行内部的在执行外部的
所以先执行 ：(1):comment = @make_p(comment)  再执行：（2） comment = @make_div(comment))
'''
#在添加一个装饰器
@make_div #添加div
@make_p  # 通过添加修饰器一来添加段落符
def comment():
    return "人生苦短，我用python！"

#需求一：改为<p>人生苦短，我用python！</p>
# print(comment())
#需求二：在需求一的基础上在添加div标签
print(comment())