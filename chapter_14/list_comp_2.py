students = {
    '喜小乐': 18,
    '石敢当': 20,
    '横小五': 15
}

# 提取 key 为一个 list
b = [key for key, value in students.items()]
print(b)

# 提取 key 为一个 tuple
b = (key for key, value in students.items())
print(b)
for x in b:
    print(x)

# key 与 value 进行颠倒
b = {value: key for key, value in students.items()}
print(b)
