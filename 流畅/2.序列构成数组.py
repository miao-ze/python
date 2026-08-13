
# list1 = ["_"] * 3

# print(list1)
# list2 = []
# for i in range(3):
#     list2.append(list1)

# print(list2)
# list2[1][1] = 'x'
# print(list2)

# list3 = []
# for i in range(3):
#     list4 = ["_"] * 3
#     list3.append(list4)
#
# print(list3)
# list3[1][1] = 'X'
# print(list3)

# list5 = [ ['_'] * 3 for i in range(3)]
# print(list5)
# list5[1][1] = 'X'
# print(list5)


# a1 = 1
# print(a1)


# str1 = 'a'
# print(id(str1))
# str1 += '2'
# print(id(str1))

# try:
#     tuple1 = (1,2,['1','2'])
#     tuple1[2] += [3,4]
# except Exception as e:
#     pass
# finally:
#     print(tuple1)


# import bisect
# list6 = [1,9,2,5,7,4,1,43]
# list7 = sorted(list6)
# print(list7)
# print(bisect.bisect(list7,10))
# list7.insert(7,10)
# print(list7)



from array import array
import random

array1 = array('d',(random.random() for i in range(10**6)))
with open('资料文件\\floats.bin', 'wb') as f:
    array1.tofile(f)

array2 = array('d')
with open('资料文件\\floats.bin', 'rb') as f:
    array2.fromfile(f,10 ** 6)

print(array2[-1])














































