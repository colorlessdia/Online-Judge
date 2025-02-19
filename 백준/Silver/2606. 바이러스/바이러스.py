import sys
from collections import deque

def BFS(graph, start):
    queue = deque([start])
    visited = [start]

    while 0 < len(queue):
        node = queue.popleft()

        for neighbor in graph[node]:

            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)

    return visited

input = sys.stdin.readline

computer = int(input())
network = int(input())

graph = dict()

for _ in range(network):
    a, b = map(int, input().split())

    if a not in graph:
        graph[a] = [b]
    else:
        graph[a] += [b]

    if b not in graph:
        graph[b] = [a]
    else:
        graph[b] += [a]

if 1 not in graph:
    print(0)
else:
    print(len(BFS(graph, 1)) - 1)