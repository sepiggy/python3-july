# 概况字符集
import re

a = 'py\rthon 1111ja\tva&67_8\nphp_'

r = re.findall('\d', a)
print(r)

r = re.findall('\D', a)
print(r)

r = re.findall('\w', a)
print(r)

r = re.findall('\W', a)
print(r)

r = re.findall('\s', a)
print(r)

