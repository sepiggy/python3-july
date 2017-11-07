class Student():
    # 类变量
    # 所有学生的总数
    sum = 0

    def __init__(self, name, age):
        # 实例变量
        self.name = name
        self.age = age
        Student.sum += 1

    def to_string(self):
        print(self.name + " " + str(self.age))

    def get_sum(self):
        print("学生总数为: " + str(Student.sum))


student1 = Student('石敢当', 18)
student2 = Student('史小诺', 19)
student1.to_string()
student2.to_string()
student2.get_sum()
