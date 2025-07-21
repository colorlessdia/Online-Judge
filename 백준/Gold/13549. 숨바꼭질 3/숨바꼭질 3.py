from collections import deque

def BFS(n):
    queue = deque([(n, 0)])
    visited = [False] * (200000 + 1)
    visited[n] = True

    while queue:
        X, sec = queue.popleft()

        if X == K:
            return sec

        d = [(X * 2, sec), (X - 1, sec + 1), (X + 1, sec + 1)]

        for i in range(3):
            dx, s = d[i]

            if not (0 <= dx <= 200000):
                continue

            if visited[dx]:
                continue

            if i == 0:
                queue.appendleft((dx, s))
            else:
                queue.append((dx, s))

            visited[dx] = True
    
    return 0

N, K = map(int, input().split())

print(BFS(N))