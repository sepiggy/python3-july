# 数量词
import re

s = 'python 1111java678php'

r = re.findall('[a-z]{3,6}', s)
print(r)
r = re.findall('[a-z]{3,6}?', s)
print(r)
