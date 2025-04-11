N, M = map(int, input().split())
J = int(input())

S = 1
E = M
T = 0

for _ in range(J):
    P = int(input())

    if S <= P <= E:
        continue
    
    if E < P:
        D = P - E

        S += D
        E += D
        T += D
        continue
    
    if P < S:
        D = S - P

        S -= D
        E -= D
        T += D
        continue

print(T)