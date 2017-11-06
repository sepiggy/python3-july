import re

# 判断 a 中是否有 Python 字符串
a = 'C|C++|Java|C#|Python|Javascript'

print(a.index('Python') > -1)

print('Python' in a)

r = re.findall('PHP', a)
if len(r) > 0:
    print('字符串中包含PHP')
else:
    print('NO')
