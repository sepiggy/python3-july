import re

language = 'PythonC#JavaC#PHPC#'


def convert(value):
    # value 是对象
    matched = value.group()
    return '!!' + matched + '!!'


# sub 函数的第二个参数可以传递一个函数
r = re.sub('C#', convert, language)
print(r)
