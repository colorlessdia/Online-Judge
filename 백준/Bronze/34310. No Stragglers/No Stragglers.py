import sys

input = sys.stdin.readline

N = int(input())

history = dict(zip(['STU', 'FAC', 'VIS'], [0, 0, 0]))

for _ in range(N):
    person_type, direction, count = input().rstrip().split()
    count = int(count)

    if direction == 'IN':
        history[person_type] += count
    elif direction == 'OUT':
        history[person_type] -= count

straggler = sum(history.values())

if not straggler:
    print('NO STRAGGLERS')
else:
    print(straggler)