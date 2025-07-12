import sys

def calc_L2_distance(x1, y1, x2, y2):
    return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

input = sys.stdin.readline

N, Q = map(int, input().split())

forward_prefix_sum = [0] * (N + 1)
reverse_prefix_sum = [0] * (N + 1)

x_list = [0] + list(map(int, input().split()))
y_list = [0] + list(map(int, input().split()))

for i in range(1, N):
    x1, y1, x2, y2 = x_list[i], y_list[i], x_list[i + 1], y_list[i + 1]
    distance = calc_L2_distance(x1, y1, x2, y2)

    if y1 == y2:
        distance *= 2
    elif y1 < y2:
        distance *= 3
    
    forward_prefix_sum[i + 1] = forward_prefix_sum[i] + distance

for i in range(N, 1, -1):
    x1, y1, x2, y2 = x_list[i], y_list[i], x_list[i - 1], y_list[i - 1]
    distance = calc_L2_distance(x1, y1, x2, y2)

    if y1 == y2:
        distance *= 2
    elif y1 < y2:
        distance *= 3
    
    reverse_prefix_sum[i - 1] = reverse_prefix_sum[i] + distance

for _ in range(Q):
    i, j = map(int, input().split())

    d1 = forward_prefix_sum[j] - forward_prefix_sum[i]
    d2 = reverse_prefix_sum[j] - reverse_prefix_sum[i]

    d = max(d1, d2)

    print(f'{d:.12f}')