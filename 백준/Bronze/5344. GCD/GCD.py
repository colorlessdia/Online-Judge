import sys

def GCD(a, b):
    if b == 0:
        return a

    return GCD(b, a % b)

n = int(sys.stdin.readline())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    A, B = max(a, b), min(a, b)
    gcd = GCD(A, B)

    print(gcd)