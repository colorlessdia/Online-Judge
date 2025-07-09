from math import pi, sin
from collections import deque

N = int(input())
queue = sorted(map(int, input().split()))

scores = deque()
temp_scores = deque()

while queue:
    scores.append(queue.pop())

    if queue:
        temp_scores.appendleft(queue.pop())

scores.extend(temp_scores)

total_polygon_area = 0
degree = (360 / N) * (pi / 180)

for i in range(N):
    r1, r2 = scores[i], scores[(i + 1) % N]

    total_polygon_area += (0.5 * r1 * r2 * sin(degree))

print(f'{total_polygon_area:.3f}')