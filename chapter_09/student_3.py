class Student():
    name = 'qiyue'
    age = 0
    gender = "boy"

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student('石敢当', 18)
student2 = Student('喜小乐', 19)

print(student1.name)
print(student2.name)
print(Student.name)
print(Student.gender)
print(student1.gender)
