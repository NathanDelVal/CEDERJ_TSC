n = 0
a = int(input())
b = int(input())

for x in range(a):
    for y in range(b):
        a = x
        b = y
        for n in range(a):
            expression = n**2 + a*n + b
            #if(expression % 2 != 0 and expression % 3 != 0 and expression % 5 != 0):
