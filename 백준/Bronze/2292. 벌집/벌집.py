N = int(input())

if N == 1:
    print(1)
else:
    a = 1
    b = 1
    i = 1

    while 1:
        c = i * 6
        b += c
        a = (b - c + 1)

        if a <= N <= b:
            break
        
        i += 1

    print(i + 1)