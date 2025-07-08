import sys

def calc_CCW(p1, p2, p3):
    v1 = (p1[0] * p2[1]) + (p2[0] * p3[1]) + (p3[0] * p1[1])
    v2 = (p1[1] * p2[0]) + (p2[1] * p3[0]) + (p3[1] * p1[0])

    return v1 - v2

def is_include(ccw1, ccw2, ccw3):
    condition1 = (0 <= ccw1) and (0 <= ccw2) and (0 <= ccw3)
    condition2 = (ccw1 <= 0) and (ccw2 <= 0) and (ccw3 <= 0)

    return condition1 or condition2

input = sys.stdin.readline

triangle_points = [0] * 3

for i in range(3):
    triangle_points[i] = tuple(map(int, input().split()))

t_a = triangle_points[0]
t_b = triangle_points[1]
t_c = triangle_points[2]

triangle_area = f'{(abs(calc_CCW(t_a, t_b, t_c)) / 2):.1f}'

N = int(input())

count = 0

for k in range(N):
    x, y = map(int, input().split())

    CCW1 = calc_CCW(t_a, t_b, (x, y))
    CCW2 = calc_CCW(t_b, t_c, (x, y))
    CCW3 = calc_CCW(t_c, t_a, (x, y))

    if is_include(CCW1, CCW2, CCW3):
        count += 1

print(triangle_area)
print(count)