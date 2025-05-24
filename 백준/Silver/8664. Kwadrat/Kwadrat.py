C = [list(map(int, input().split())) for _ in range(4)]
C.sort(key=lambda x: (x[0], x[1]))

x1, y1 = C[0]
x2, y2 = C[1]
x3, y3 = C[2]
x4, y4 = C[3]

is_valid = False

if x1 == x2 and y1 != y2:
    side = abs(y2 - y1)

    c1 = x1 + side == x3 and y1 == y3
    c2 = x2 + side == x4 and y2 == y4

    if c1 and c2 and 1:
        is_valid = True

if is_valid:
    print('TAK')
else:
    print('NIE')