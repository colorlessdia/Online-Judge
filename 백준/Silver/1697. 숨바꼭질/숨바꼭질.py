from collections import deque

def BFS(N, K):
    queue = deque([(N, 0)])
    visited = set([N])

    if N == K:
        return 0

    while queue:
        x, sec = queue.popleft()

        dx = [x * 2, x + 1, x - 1]

        for i in range(3):
            X = dx[i]

            if X in visited:
                continue

            if not (-10 ** 5 <= X <= 10 ** 5):
                continue

            if X == K:
                return sec + 1
            
            queue.append((X, sec + 1))
            visited.add(X)

N, K = map(int, input().split())

print(BFS(N, K))