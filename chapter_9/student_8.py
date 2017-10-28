class Student(object):
    sum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

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


student1 = Student('史小诺', 18)
student1.add(1, 2)
Student.add(1, 2)
