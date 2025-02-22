N, m, M, T, R = map(int, input().split())

time = 0
X = m

while 0 < N:
    time += 1

    if X + T <= M:
        X += T
        N -= 1
        continue
    
    temp = max(X - R, m)

    if temp == X:
        time = -1
        break

    X = temp

print(time)