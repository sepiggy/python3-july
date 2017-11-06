# 全局变量
name = "Jms"
age = 200


class Student():
    # 类变量
    name = ''
    age = 0

    # 构造函数
    def __init__(self, name, age):
        # 特征, 定义实例变量
        self.name = name
        self.age = age
        # print("student...")

    # 行为
    def do_homework(self):
        print('do homework...')

    # def print_file(self):
    #     print('name: ' + self.name)
    #     print('age: ' + str(self.age))
    #     print(name)
    #     print(age)


class StudentHomework():
    homework_name = ''

# student = Student()
# student.print_file()

student1 = Student("xxx", 19)
print(type(student1))
print(student1.name)

