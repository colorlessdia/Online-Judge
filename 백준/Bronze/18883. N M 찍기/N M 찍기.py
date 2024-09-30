import sys

N, M = map(int, sys.stdin.readline().split())

count = 1

for _ in range(N):
    temp = [0] * M

    for i in range(M):
        temp[i] = count
        count += 1
    
    print(*temp)