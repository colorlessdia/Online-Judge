N = int(input())
D_list = sorted(map(int, input().split()))
M = (N + 1) // 2

low_tide_group = D_list[:M][::-1]
high_tide_group = D_list[M:]
sorted_group = []

for i in range(len(high_tide_group)):
    sorted_group.append(low_tide_group[i])
    sorted_group.append(high_tide_group[i])

if N % 2 != 0:
    sorted_group.append(low_tide_group[-1])

print(*sorted_group)