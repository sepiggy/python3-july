# 组

import re

a = 'PythonPythonPythonPythonPython'

# 判断字符串中是否包含 3 个 Python
# r = re.findall('PythonPythonPython', a)
# r = re.findall('(Python){1,}?', a)
r = re.findall('(Python){3}', a)
print(r)
