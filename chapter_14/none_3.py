class Test():
    def __len__(self):
        return 1


test = Test()
print(bool(None))
print(bool([]))
print(bool(test))


if test:
    print('T')
else:
    print('F')
