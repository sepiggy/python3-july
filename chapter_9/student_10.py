from human import Human

# 继承
class Student(Human):

    def __init__(self, name, age, school):
        # Human.__init__(self, name, age)
        self.school = school
        super(Student, self).__init__(name, age)

    def do_homework(self):
        print('do homework...')


student1 = Student('史小诺', 25, '新华中学')
print(student1.sum)
print(Student.sum)
print(student1.name)
print(student1.age)
student1.get_name()

