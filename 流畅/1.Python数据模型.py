from collections import namedtuple

# student_document = namedtuple('student_Information',['class_room','name'])
# i = student_document('高一（1班）','阿斯顿')
# print(i)
# print(student_document)


# a = int('3')
# print(a)

class Int():
    def __init__(self,num):
        self._num = num

    def __repr__(self):
        return 'int{}'.format(int(self._num))

    def __getitem__(self, item):
        return self._num[item]

a = Int('3asfa')

