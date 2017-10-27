import re

# 获取 life 和 python 中间的字符 (爬虫用)
s = 'life is short, i use python'

r = re.search('life(.*)python', s)
print(r.group(0))
print(r.group(1))

# 等价于
r = re.findall('life(.*)python', s)
print(r)
