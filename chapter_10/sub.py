import re

language = 'PythonC#JavaC#PHPC#'

# r = re.sub('C#', 'Go', language, 1)
# Python 内置的字符串处理函数
r = language.replace('C#', 'Go')
print(language)
print(r)

replace = 'HelloWorldHelloWorld'.replace('Hello', 'Hi')
print(replace)
# print(r)
