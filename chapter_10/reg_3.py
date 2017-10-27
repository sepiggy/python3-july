import re

s = 'abc,acc,adc,aec,afc,ahc'

r = re.findall('a[cf]c', s)
print(r)

r = re.findall('a[^cfd]c', s)
print(r)
