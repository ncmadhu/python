
test = [lambda: x + 1 for x in range(4)]
for i in range(4):
    print test[i]()
