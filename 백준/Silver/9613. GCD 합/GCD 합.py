import sys

def GCD(a, b):
    if b == 0:
        return a

    return GCD(b, a % b)

t = int(sys.stdin.readline())

for _ in range(t):
    line = list(map(int, sys.stdin.readline().split()))
    n, number_list = line[0], sorted(line[1:], key=lambda x: -x)

    total = 0

    for i in range(n):
        for j in range(i + 1, n):
            total += GCD(number_list[i], number_list[j])
    
    print(total)