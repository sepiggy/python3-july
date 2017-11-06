from student import Student

student1 = Student()
student2 = Student()
student3 = Student()

student_id1 = hex(id(student1))
student_id2 = hex(id(student2))
student_id3 = hex(id(student3))

print(student_id1)
print(student_id2)
print(student_id3)