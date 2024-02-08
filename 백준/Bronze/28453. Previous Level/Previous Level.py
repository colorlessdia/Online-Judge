N = int(input())
M = list(map(int, input().split()))

level_list = [0] * N

for i, level in enumerate(M):
    if 300 == level:
        level_list[i] = 1
    elif 275 <= level:
        level_list[i] = 2
    elif 250 <= level:
        level_list[i] = 3
    else:
        level_list[i] = 4

print(*level_list)