"""制作个人信息调查表"""
# class People():
#     city = '北京'
#     def __init__(self,name,age,hobby,app):
#         self.name = name
#         self.age = age
#         self.hobby = hobby
#         self.app = app
#     @staticmethod
#     def print_menu():
#         print('-------个人信息--------')
#     def print_info(self):
#         print('居住城市：',People.city)
#         print('姓名：', self.name)
#         print('年龄：', self.age)
#         print('爱好：', self.hobby)
#         print('常用APP：', self.app)
# people1 = People('缪泽平','20','看番','稀饭动漫')
# people1.print_menu()
# people1.print_info()





'''猫狗大战'''
class Animal:
    '''初始化动物的昵称，品种，攻击力，生命值'''
    def __init__(self,name,breed,fight,life_value):
        self.name = name
        self.breed = breed
        self.fight = int(fight)
        self.life_value = int(life_value)
    '''定义攻击方法，并判断是否死亡'''
    def attack(self,animal):
        animal.life_value -= self.fight
        if animal.life_value <= 0:
            print(f'{self.name}攻击{animal.name}一次，{animal.name}被杀死')
            return True
        else:
            print(f'{self.name}攻击{animal.name}一次，{animal.name}的生命值还有{animal.life_value}')
    def eat(self):
        pass
    def message(self):
        print(f'昵称：{self.name},品种：{self.breed},攻击力:{self.fight},生命值：{self.life_value}')

class Cat(Animal):
    '''重写增长生命值的方法'''
    def eat(self):
        self.life_value += 50
        print(f'{self.name}增加一次生命值，还有生命值{self.life_value}')
class Dog(Animal):
    def eat(self):
        self.life_value += 30
        print(f'{self.name}增加一次生命值，还有生命值{self.life_value}')

print('----------角色信息---------')
cat = Cat('加菲猫','黄猫','30','200')
cat.message()
dog = Dog('乔治','黑狗','40','200')
dog.message()
print('****************战斗开始***************\n'
      '****k键控制猫攻击，l键控制猫增加生命值*****\n'
      '****-键控制狗攻击，+键控制狗增加生命值****')
while True:
    order = input('请输入您的战斗方式：')
    if order == 'k':
        if cat.attack(dog):  #当猫杀死狗是用于返回值是true所以此时判断成立执行break终止循环
            break
    elif order == '-':
        if dog.attack(cat):
            break
    if order == 'l':
        cat.eat()
    elif order == '+':
        dog.eat()


































