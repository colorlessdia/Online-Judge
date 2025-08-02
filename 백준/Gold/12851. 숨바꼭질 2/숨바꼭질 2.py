from collections import deque

def BFS(n, k):
    queue = deque([n])
    dist = [-1] * (200000 + 1)
    count = [0] * (200000 + 1)

    dist[n] = 0
    count[n] = 1

    while queue:
        x = queue.popleft()

        for X in [x * 2, x + 1, x - 1]:

            if not (0 <= X <= 200000):
                continue

            if dist[X] == -1:
                dist[X] = dist[x] + 1
                count[X] = count[x]

                queue.append(X)
                continue

            if dist[X] == dist[x] + 1:
                count[X] += count[x]
    
    return dist[k], count[k]

N, K = map(int, input().split())

T, C = BFS(N, K)

print(T)
print(C)