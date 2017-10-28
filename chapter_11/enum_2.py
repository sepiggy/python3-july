import enum


class VIP(enum.Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


class VIP1(enum.Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


result = VIP.GREEN == VIP.BLACK
result = VIP.GREEN == "2"
# result = VIP.GREEN > VIP.BLACK
result = VIP.GREEN is VIP.GREEN
result = VIP.GREEN == VIP1.GREEN
print(result)
