# 边界匹配

import re

# qq = '123456789'
qq = '100000001'

# r = re.findall('^\d{4,8}$', qq)
r = re.findall('^10001$', qq)

print(r)
