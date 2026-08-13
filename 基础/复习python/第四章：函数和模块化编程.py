

# 实例4.1 阶层函数
# def fact(n):
#     """
#     :function:计算阶层
#     :param n: int > 0
#     :return: result
#     """
#     result = 1
#     for i in range(1,n+1):
#         result *= i
#     return result
# if __name__ == '__main__':
#     result = fact(5)
#     print(result)

# 实例4.2 素数函数
# def is_prime(n):
#     """
#     function: 判断素数
#     :param n: int
#     :return: None
#     """
#     if n == 1 or n == 2:
#         print(f'{n}是素数')
#         return
#     for i in range(2,n):
#         if n % i == 0:
#             print(f'{n}不是素数')
#             return
#     print(f'{n}是素数')

# n = int(input('n: '))
# is_prime(n)

# 实例4.3 幂函数
# def power(x,n):
#     result = 1
#     for i in range(n):
#         result = result * x
#     return result
#
#
# x = eval(input('x: '))
# n = eval(input('n: '))
# print(power(x,n=n ))


# 实例4.5 回文素数
# from Calc import is_prime
#
# def is_all(num):
#     result = is_prime(num)
#     if result is True:
#         str_num = str(num)
#         if str_num == str_num[::-1]:
#             return f'{num}是回文素数'
#         else:
#             return f'{num}不是回文素数'
#     else:
#         return f'{num}不是回文素数'
#
# while True:
#     num =int(input('num: '))
#     result = is_all(num)
#     print(result)


# 本章练习
# （1）
def binary_sqrt(n: float, epsilon: float = 1e-6) -> float:
    """
    使用二分法计算非负实数的算术平方根
    :param n: 待开方的非负实数，要求 n >= 0
    :param epsilon: 计算精度，默认1e-6（误差不超过百万分之一）
    :return: 平方根的近似值
    """
    # 1. 参数合法性校验
    if n < 0:
        raise ValueError("n 必须大于等于 0，负数无实数平方根")

    # 2. 特殊值直接返回
    if n == 0:
        return 0.0

    # 3. 初始化二分区间
    left = 0.0
    right = max(1.0, n)  # 统一处理n<1和n>=1两种场景

    # 4. 二分迭代，直到区间长度小于精度要求
    while right - left > epsilon:
        mid = (left + right) / 2  # 取区间中点
        mid_square = mid * mid  # 计算中点的平方

        if mid_square > n:
            # 中点平方大于n，根在左半区间，缩小右边界
            right = mid
        else:
            # 中点平方小于等于n，根在右半区间，缩小左边界
            left = mid

    # 5. 返回区间中点作为最终近似结果
    return (left + right) / 2

print(binary_sqrt(5,1e-6))










































