K = int(input())
A, B = 1, 0

for _ in range(K):
    a, b = B, (A + B)
    A, B = a, b

print(A, B)