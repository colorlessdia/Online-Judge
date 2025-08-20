import sys
from collections import deque

def calc_L1_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def BFS(points):
    queue = deque()
    queue.append(points[0])
    visited = [False] * (N + 2)
    visited[0] = True

    while queue:
        x1, y1 = queue.popleft()

        for i in range(N + 2):

            if visited[i]:
                continue

            x2, y2 = points[i]
            distance = calc_L1_distance(x1, y1, x2, y2)

            if 1000 < distance:
                continue

            if i == N + 1:
                return 'happy'
            
            queue.append((x2, y2))
            visited[i] = True
    
    return 'sad'

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    point_list = [tuple(map(int, input().split())) for _ in range(N + 2)]

    print(BFS(point_list))