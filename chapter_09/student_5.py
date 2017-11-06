# 类与对象的变量查找顺序

class Student():
    name = 'qiyue'
    age = 0

    def __init__(self, name, age):
        name = name
        age = age


student1 = Student('石敢当', 18)
print(student1.__dict__)
print(student1.name)
print(Student.name)

