n = int(input())

if n == 0:
    print(0)
elif n < 3:
    print(1)
else:
    before_2 = 1
    before_1 = 1
    current = before_2 + before_1

    for i in range(3, n):
        before_2 = before_1
        before_1 = current
        current = before_2 + before_1

        if 1000000007 <= current:
            current %= 1000000007
    
    print(current)