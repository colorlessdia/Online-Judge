a, b = map(int, input().split())

A, B = max(a, b), min(a, b)

while B != 0:
    A, B = B, A % B

print(A)