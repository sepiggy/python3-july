list_x = [1, 0, 1, 0, 0, 1]

# r = filter(lambda x: True if x == 1 else False, list_x)
r = filter(lambda x: x, list_x)
print(list(r))
