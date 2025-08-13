import sys

def calc_polygon_area(points, length):
    sum1 = 0
    sum2 = 0

    for i in range(length):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % length]

        sum1 += x1 * y2
        sum2 += y1 * x2
    
    return (sum1 - sum2) / 2

input = sys.stdin.readline

N, V = map(int, input().split())

total_polygon_area = 0

for i in range(N):
    K = int(input())
    
    CW_points = [tuple(map(int, input().split())) for _ in range(K)]
    total_polygon_area += calc_polygon_area(CW_points, K)

height = V /total_polygon_area

print(f'{height:.9f}')