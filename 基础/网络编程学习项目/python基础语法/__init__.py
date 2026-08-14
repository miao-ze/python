class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_info(self):
        print(f'洗衣机型号：{self.name}')
        print(f'宽度：{self.width}cm')
        print(f'高度：{self.height}cm')


# 正确执行3次循环
for i in range(1, 4):
    # 输入洗衣机数据（非冰箱）
    model = input(f"请输入第{i}台洗衣机的型号：")
    width = int(input('宽度(cm)：'))
    height = int(input('高度(cm)：'))

    # 正确实例化Washer对象
    washer = Washer(width, height)
    washer.name = model  # 正确设置型号属性

    washer.print_info()  # 输出信息