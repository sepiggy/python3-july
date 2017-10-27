import re

s='A83C72D1D8E67'

def convert(value):
    matched = value.group()
    if int(matched) >=50:
        return '100'
    else:
        return '0'


sub = re.sub('\d{2}', convert, s)
print(sub)
