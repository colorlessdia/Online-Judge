N = int(input())
X = int(input())

T = 0

for _ in range(N):
    P1, P2 = map(int, input().split())
    D = max(P1, P2) - min(P1, P2)

    if D <= X:
        T += max(P1, P2)
        continue
    
    P3 = int(input())

    T += P3

print(T)