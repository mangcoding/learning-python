n = 10
a = 0
b = 1
c = 0
d = 0

for i in range(n):
    d = a+b+c
    a = b
    b = c
    c = d
    print(d, end=' ')