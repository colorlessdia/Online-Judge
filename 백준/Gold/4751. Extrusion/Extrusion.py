import sys

def calc_polygon_area(points, length):
    sum1 = 0
    sum2 = 0

    for i in range(length):
        sum1 += points[i][0] * points[(i + 1) % length][1]
        sum2 += points[i][1] * points[(i + 1) % length][0]

    return (abs(sum1 - sum2) / 2)

input = sys.stdin.readline

while 1:
    N = int(input())

    if N < 3:
        break
    
    points = [tuple(map(float, input().split())) for _ in range(N)]

    volume = float(input())
    area = calc_polygon_area(points, N)

    bar_length = volume / area

    print(f'BAR LENGTH: {bar_length:.2f}')