b2 = 0
b1 = 1

n = int(input())

if n == 0:
    print(b2)
elif n == 1:
    print(b1)
else:
    for i in range(2, n + 1):
        cur = b2 + b1
        
        if i == n:
            print(cur)
        
        b2 = b1
        b1 = cur