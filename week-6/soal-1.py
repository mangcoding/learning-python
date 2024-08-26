n = 10
a = 1
b = 1
c = 2

for i in range(n):
    if (i == 0 or i == 1):
        c = 1
    else:
        c = a+b
    a = b
    b = c
    print(c, end=' ')
