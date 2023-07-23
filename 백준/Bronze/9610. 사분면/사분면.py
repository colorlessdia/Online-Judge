import sys

pos = [0] * 5

for _ in range(int(input())):
    x, y = map(int, sys.stdin.readline().split())
    
    if 0 < x and 0 < y:
        pos[0] += 1
    elif x < 0 and 0 < y:
        pos[1] += 1
    elif x < 0 and y < 0:
        pos[2] += 1
    elif 0 < x and y < 0:
        pos[3] += 1
    else:
        pos[4] += 1
    
for i, p in enumerate(pos, 1):
    if i != len(pos):
        print(f'Q{i}: {p}')
    else:
        print(f'AXIS: {p}')