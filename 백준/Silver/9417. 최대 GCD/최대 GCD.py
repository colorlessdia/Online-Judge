import sys

def GCD(a, b):
    if b == 0:
        return a
    
    return GCD(b, a % b)

N = int(sys.stdin.readline())

for _ in range(N):
    line = sorted(map(int, sys.stdin.readline().split()), key=lambda x: -x)

    max_gcd = 0

    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            gcd = GCD(line[i], line[j])

            if max_gcd < gcd:
                max_gcd = gcd

    print(max_gcd)