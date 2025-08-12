import sys

def calc_polygon_area(points, length):
    sum1 = 0
    sum2 = 0

    for i in range(length):
        
        if i < length - 1:
            sum1 += points[i][0] * points[i + 1][1]
            sum2 += points[i][1] * points[i + 1][0]
            continue
        
        sum1 += points[i][0] * points[0][1]
        sum2 += points[i][1] * points[0][0]
    
    return abs(sum1 - sum2) / 2

input = sys.stdin.readline

N = int(input())

total_polygon_area = 0

for _ in range(N):
    P = int(input())
    points = [tuple(map(int, input().split())) for _ in range(P)]

    total_polygon_area += calc_polygon_area(points, P)

print(int(total_polygon_area))