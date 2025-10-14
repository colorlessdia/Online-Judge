import sys

input = sys.stdin.readline

N = int(input())

candidates = []

for _ in range(N):
    line = input().rstrip().split()
    
    name = line[0]
    is_jaehak = True if line[1] == 'jaehak' else False
    is_winner = True if line[2] == 'winner' else False
    is_rank = True if 1 <= int(line[3]) <= 3 else False
    apc_rank = int(line[4])

    if (
        (is_jaehak) and
        (not is_winner) and
        (not is_rank)
    ):
        candidates.append((name, apc_rank))

candidates.sort(key=lambda x: x[1])
count = min(10, len(candidates))
candidates = candidates[:count]
candidates.sort(key=lambda x: x[0])

print(count)

for finalist, _ in candidates:
    print(finalist)