#!/usr/bin/python3
for i in range(0, 9):
    a = i + 1
    while a <= 9:
        if a == 9 and i == 8:
            print(89)
        else:
            print('{}{}'.format(i, a), end=', ')
        a += 1
