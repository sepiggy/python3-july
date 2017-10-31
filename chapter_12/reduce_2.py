from functools import reduce

list_x = ['1', '2', '3', '4', '5']
# reduce 实现字符串拼接
s = reduce(lambda x, y: x + y, list_x, 'aaaaa')
print(s)
