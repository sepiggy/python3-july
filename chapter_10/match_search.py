import re

s = '83C72D1D8E67'

match = re.match('\d', s)
print(match.span())

search = re.search('\d', s)
print(search.group())
