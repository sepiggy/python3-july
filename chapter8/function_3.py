# 默认参数

def print_student_files(name, gender='男', age=18, college='人民路小学'):
    print('我叫' + name)
    print('我今年' + str(age) + '岁')
    print('我是' + gender + '生')
    print('我在' + college + '上学')

print_student_files('王二小', '男', 18, '人民路小学')
print_student_files('王二小')
