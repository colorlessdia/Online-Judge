N = int(input())
T_list = list(map(int, input().split()))

day, min_T = -1, 41

for i in range(N - 2):
    T1, _, T3 = T_list[i:i + 3]
    T = max(T1, T3)

    if T < min_T:
        day = i + 1
        min_T = T

print(day, min_T)