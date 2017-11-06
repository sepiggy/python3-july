# 在实例方法中访问实例变量与类变量

class Student():
    stu_sum = 0
    name = 'qiyue'
    age = 0

    def __init__(self, name1, age):

        self.name = name1
        self.age = age
        print(self.name)
        print(self.__dict__)
        print(self.__class__.name)


student1 = Student("史小诺", 25)
