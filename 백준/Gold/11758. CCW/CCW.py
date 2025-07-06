P_list = [list(map(int, input().split())) for _ in range(3)]

x1, y1 = P_list[0]
x2, y2 = P_list[1]
x3, y3 = P_list[2]

CCW = ((x1 * y2) + (x2 * y3) + (x3 * y1)) - ((y1 * x2) + (y2 * x3) + (y3 * x1))

if CCW == 0:
    print(0)
elif 0 < CCW:
    print(1)
elif CCW < 0:
    print(-1)