from enum import IntEnum
from enum import unique

@unique
class VIP(IntEnum):
    # YELLOW = '1'
    # GREEN = 'str'
    YELLOW = 1
    GREEN = 1
    BLACK = 3
    RED = 4

for v in VIP:
    print(v.name)



