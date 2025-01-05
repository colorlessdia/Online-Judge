n = int(input())

if 0 <= n:
    print(len(bin(n)[2:]))
else:
    print(32)