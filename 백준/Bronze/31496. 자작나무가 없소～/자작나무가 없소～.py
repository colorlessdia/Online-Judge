import sys

input = sys.stdin.readline

N, S = input().rstrip().split()
N = int(N)

total_count = 0

for _ in range(N):
    item, count = input().rstrip().split()
    item_set = set(item.split('_'))
    count = int(count)

    if S in item_set:
        total_count += count

print(total_count)