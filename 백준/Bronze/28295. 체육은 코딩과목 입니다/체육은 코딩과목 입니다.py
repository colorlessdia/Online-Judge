import sys

deg = 0

for _ in range(10):
    t = int(sys.stdin.readline())

    if t == 1:
        deg += 90
    elif t == 2:
        deg += 180
    elif t == 3:
        deg -= 90

d = deg % 360

if d == 0:
    print('N')
elif d == 90:
    print('E')
elif d == 180:
    print('S')
elif d == 270:
    print('W')