import sys

X, Y = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
direction = sys.stdin.readline().rstrip()

valid_count = []
valid_square = [
    (X, Y),
    (X, Y + 1),
    (X, Y - 1),
    (X + 1, Y),
    (X + 1, Y + 1),
    (X + 1, Y - 1),
    (X - 1, Y),
    (X - 1, Y + 1),
    (X - 1, Y - 1),
]

x, y = 0, 0

if (x, y) in valid_square:
    valid_count.append(0)

for i, d in enumerate(direction, 1):
    
    if d == 'I':
        x += 1
    elif d == 'Z':
        x -= 1
    elif d == 'S':
        y += 1
    elif d == 'J':
        y -= 1
    
    if (x, y) in valid_square:
        valid_count.append(i)

if len(valid_count) == 0:
    print(-1)
else:
    
    for count in valid_count:
        print(count)