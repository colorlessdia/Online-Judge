import sys

input = sys.stdin.readline

N = int(input())

max_list = [0, 0, 0]
min_list = [0, 0, 0]
sequence = [[0, 2], [0, 3], [1, 3]]

for _ in range(N):
    line = list(map(int, input().split()))

    max_temp = [0, 0, 0]
    min_temp = [0, 0, 0]

    for i in range(2 + 1):
        s, e = sequence[i]

        max_temp[i] += line[i] + max(max_list[s:e])
        min_temp[i] += line[i] + min(min_list[s:e])

    max_list = max_temp
    min_list = min_temp

print(max(max_list), min(min_list))