import sys
from collections import deque

def BFS(graph, start):
    queue = deque([start])
    visited = deque([start])

    while 0 < len(queue):
        node = queue.popleft()

        for neighbor in sorted(graph[node]):
            
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    return visited

input = sys.stdin.readline

N, M = map(int, input().split())

graph = dict(zip(range(1, N + 1), [[] for _ in range(N)]))

for _ in range(M):
    u, v = map(int, input().split())

    graph[u] += [v]
    graph[v] += [u]

start_point_dict = dict(zip(range(1, N + 1), [1] * N))

count = 0

for i in range(1, N + 1):
    
    if i not in start_point_dict:
        continue
    
    for start_point in BFS(graph, i):
        del start_point_dict[start_point]
    
    count += 1

print(count)