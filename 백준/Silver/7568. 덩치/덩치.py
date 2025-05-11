import sys

input = sys.stdin.readline

N = int(input())

size_list = [list(map(int, input().split())) for _ in range(N)]
count_list = [0] * N

for i in range(N):
    ax, ay = size_list[i]
    count = 1
    
    for j in range(N):
        bx, by = size_list[j]

        if i == j:
            continue

        if ax < bx and ay < by:
            count += 1

    count_list[i] = count

print(*count_list)