from enum import Enum


class VIP(Enum):
    YELLOW = 1
    # YELLOW = 2 报错
    GREEN = 2
    BLACK = 3
    RED = 4


class Common():
    YELLOW = 1
    YELLOW = 2


print(VIP.YELLOW)
print(VIP.YELLOW.name)
print(VIP.YELLOW.value)
print(type(VIP.YELLOW))
print(type(VIP.YELLOW.name))
print(VIP['YELLOW'])

# 遍历枚举类型
for v in VIP:
    print(v)

# VIP.YELLOW = 6 报错
Common.YELLOW = 6
