T = int(input())

A, B, C = 300, 60, 10

a = T // A
T %= A

b = T // B
T %= B

c = T // C
T %= C

print(a, b, c) if T == 0 else print(-1)