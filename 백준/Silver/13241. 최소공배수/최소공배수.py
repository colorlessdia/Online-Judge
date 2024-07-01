def GCD(a, b):
    if b == 0:
        return a

    return GCD(b, a % b)

A, B = map(int, input().split())

LCM = A * B // GCD(max(A, B), min(A, B))

print(LCM)