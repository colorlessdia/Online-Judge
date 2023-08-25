import sys

for _ in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    mul = a * b

    if a < b:
        a, b = b, a

    while 1:
        a, b = b, a % b

        if b == 0:
            print(mul // a)
            break