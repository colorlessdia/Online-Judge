import sys
from collections import deque

def BFS():
    queue = deque([(1, 0)])
    visited = [False] * (100 + 1)
    visited[1] = True

    while queue:
        current_number, count = queue.popleft()

        if current_number == 100:
            return count

        for i in range(1, 6 + 1):
            next_number = current_number + i

            if 100 < next_number:
                continue

            if next_number in ladder_dict:
                next_number = ladder_dict[next_number]
            elif next_number in snake_dict:
                next_number = snake_dict[next_number]

            if visited[next_number]:
                continue
            
            queue.append((next_number, count + 1))
            visited[next_number] = True
    
    return 0

input = sys.stdin.readline

N, M = map(int, input().split())

ladder_dict = dict()
snake_dict = dict()

for _ in range(N):
    x, y = map(int, input().split())

    ladder_dict[x] = y

for _ in range(M):
    u, v = map(int, input().split())

    snake_dict[u] = v

print(BFS())