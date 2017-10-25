class Student():
    sum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__score = 0

    @classmethod
    def plus_sum(cls):
        cls.sum += 1

    @classmethod
    def get_sum(cls):
        return cls.sum

    @staticmethod
    def add(x, y):
        print(Student.sum)
        print('This is a static method...')

    def marking(self, score):
        if score < 0:
            return '分数为负, 错误'
        self.__score = score
        return score


student1 = Student('史小诺1', 18)
student2 = Student('史小诺2', 19)

result = student1.marking(59)
# 为 Student 新加了一个实例变量
student1.__score = -1
print(student1.__score)
print(student1.__dict__)

# print(student2.__score)
print(student2._Student__score)
print(student2.__dict__)
# print(result)
