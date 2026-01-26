N = int(input())

S = ''

for i in range(1, N + 1):
    D = str(i)

    if D not in S:
        S += D

print(S)