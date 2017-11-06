# 类方法

class Student():
    sum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_sum(self):
        print("学生总数为: " + str(self.__class__.sum))

    # 类方法
    @classmethod
    def plus_sum(cls):
        cls.sum += 1

student1 = Student('王一', 20)
Student.plus_sum()
student2 = Student('王二', 19)
Student.plus_sum()
student3 = Student('王三', 18)
Student.plus_sum()

student1.print_sum()
