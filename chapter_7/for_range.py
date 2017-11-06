for x in range(10, 0, -2):
    print(x, end='|')
print()

# 截取奇数序列
a = [1, 2, 3, 4, 5, 6, 7, 8]

# 使用 for-range 实现
for i in range(0, len(a), 2):
    print(a[i], end="|")
print()

# 使用切片实现 (better)
b = a[0:len(a):2]
print(b)