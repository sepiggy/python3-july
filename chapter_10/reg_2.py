import re

# 提取 a 中的所有数字
a = 'C0C++7Java8C#9Python6Javascript'

r = re.findall('\d', a)
print(r)

r = re.findall('\D', a)
print(r)
