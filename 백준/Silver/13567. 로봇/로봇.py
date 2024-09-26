import sys

M, N = map(int, sys.stdin.readline().split())

x, y = 0, 0

direction_sequence = ['E', 'S', 'W', 'N']
direction_index = 0
direction = direction_sequence[direction_index]

is_valid = True

for i in range(N):
    command = sys.stdin.readline().rstrip().split()

    if command[0] == 'TURN' and command[1] == '1':
        direction_index += 1

        if 3 < direction_index:
            direction_index = 0

        direction = direction_sequence[direction_index]
        continue

    if command[0] == 'TURN' and command[1] == '0':
        direction_index -= 1

        if direction_index < 0:
            direction_index = 3

        direction = direction_sequence[direction_index]
        continue
    
    if command[0] == 'MOVE':
        distance = int(command[1])

        if direction == 'E':
            x += distance
        elif direction == 'W':
            x -= distance
        elif direction == 'N':
            y += distance
        elif direction == 'S':
            y -= distance

    if not (0 <= x <= M) or not(0 <= y <= M):
        is_valid = False

if is_valid:
    print(x, y)
else:
    print(-1)