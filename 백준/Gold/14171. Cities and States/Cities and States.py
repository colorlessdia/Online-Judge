import sys

input = sys.stdin.readline

N = int(input())

pair_count = dict()

for _ in range(N):
    city, state_code = input().rstrip().split()
    city_code = city[:2]

    if state_code == city_code:
        continue

    pair = (state_code, city_code)
    pair_count[pair] = pair_count.get(pair, 0) + 1

total_count = 0

for current_pair, count in pair_count.items():
    target_pair = (current_pair[1], current_pair[0])

    if target_pair < current_pair:
        continue

    if target_pair not in pair_count:
        continue
    
    target_count = pair_count[target_pair]
    total_count += (count * target_count)

print(total_count)