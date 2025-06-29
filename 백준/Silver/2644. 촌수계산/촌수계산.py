from collections import deque

def BFS(graph, start, end):
    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        number, count = queue.popleft()

        if number == end:
            return count

        for neighbor in graph.get(number, []):
            
            if neighbor not in visited:
                queue.append((neighbor, count + 1))
                visited.add(neighbor)
        
    return -1

N = int(input())
A, B = map(int, input().split())
M = int(input())

graph = dict()

for _ in range(M):
    X, Y = map(int, input().split())

    if X not in graph:
        graph[X] = []
    
    if Y not in graph:
        graph[Y] = []

    graph[X].append(Y)
    graph[Y].append(X)

print(BFS(graph, A, B))