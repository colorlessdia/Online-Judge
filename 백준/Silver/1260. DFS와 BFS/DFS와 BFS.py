import sys
from collections import deque

def DFS(graph, node, visited=deque()):
    
    if node not in visited:
        visited.append(node)

        for neighbor in sorted(graph[node]):
            DFS(graph, neighbor, visited)
    
    return visited

def BFS(graph, start):
    queue = deque([start])
    visited = deque([start])

    while 0 < len(queue):
        node = queue.popleft()

        for neighbor in sorted(graph[node]):
            
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
    
    return visited

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = dict(zip(range(1, N + 1), [[] for _ in range(N)]))

for _ in range(M):
    A, B = map(int, input().split())

    graph[A] += [B]
    graph[B] += [A]

print(*DFS(graph, V))
print(*BFS(graph, V))