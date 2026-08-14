user_message = []
def system():

    print('**' * 10)
    # user_input = int(input('请输入您要查询的内容：'))
    print(' 1.添加客户的信息    2.删除客户的信息        3.更改用户的积分信息\n '
          '4.查询客户的信息    5.显示所有客户的信息     6.保存客户的信息\n'
          ' 7.读取用户的信息    0.退出系统')
    print('=='*10)

"""1.定义添加客户的信息"""
def add_user():
    user_name = input('请输入需要添加的名字: ')
    user_dit = {}
    user_mul = int(input('请输入用户您的编号：'))
    user_sex = input('请输入用户您的性别：')
    user_count = input('请输入用户您的积分：')
    user_dit['姓名'] = user_name
    user_dit['编号'] = user_mul
    user_dit['性别'] = user_sex
    user_dit['积分'] = user_count
    user_message.append(user_dit)
    print('用户已添加完成')

"""2.定义删除用户的信息"""
def del_user():
    uesr_name = input('请输入需要删除用户的姓名：')
    for name in user_message:   #此时name 为字典
        if name['姓名'] == uesr_name:
            user_message.remove(name)
            print('已删除该用户')
            return
        print('该用户不存在')

'''3.定义更改用户的积分信息'''
def change_count():
    uesr_name = input('请输入需要更改用户积分的姓名：')
    for name in user_message:   #此时name 为字典
        if name['姓名'] == uesr_name:
            change = int(input('请输入更改过的信息：'))
            name['积分'] = change
            print(f'此时用户的信息为：{name}')

"""4.定义查询用户信息"""
def look_user():
    uesr_name = input('请输入需要查询用户信息人的姓名：')
    for name in user_message:   #此时name 为字典
        if name['姓名'] == uesr_name:
            print(f'姓名：{name['姓名']},编号 ：{name['编号']},性别 ：{name['性别']},积分 ：{name['积分']}')
        else:
            return '查无此人'

"""5.定义显示所用用户的信息"""
def all_look_user():
        for name in user_message:
            print(name)

"""6.定义保存用户的信息"""
def save_user():
    with open('客户信息.txt','a+',encoding='utf-8') as file:
        # file.write('%s%10s%10s%10s\n' % ('姓名','编号','性别','积分'))
        for name in user_message:

            file.write(f'姓名：{name['姓名']},编号 ：{name['编号']},性别 ：{name['性别']},积分 ：{name['积分']}\n')


'''7.读取用户的信息'''
def read_user():
    try:
        with open('客户信息.txt','r',encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())
    except FileExistsError:
        print("文件 '客户信息.txt' ,不存在 ")



def main():
    while True:
        system()
        user_input = int(input('请输入您要查询的内容：'))

        if user_input == 1:
            add_user()
            continue
        elif user_input == 2:
            del_user()
            continue
        elif user_input == 3:
            change_count()
            continue
        elif user_input == 4:
            look_user()
            continue
        elif user_input == 5:
            all_look_user()
            continue
        elif user_input == 6:
            save_user()
            continue
        elif user_input == 7:
            read_user()
        elif user_input == 0:
            quit_con = input('您确定要退出吗？（y or n）')
            if quit_con == 'y':
                break

print('客户信息管理系统（文件版）')
main()
















