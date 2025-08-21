from collections import deque

def BFS(n):
    queue = deque([(n, 0)])
    limit = 99999
    visited = [False] * (limit + 1)
    visited[n] = True

    d = [10000, 1000, 100, 10, 1]

    while queue:
        number, count = queue.popleft()

        if T < count:
            continue

        if number == G:
            return count

        if number + 1 <= limit:
            A = number + 1

            if not visited[A]:
                queue.append((A, count + 1))
                visited[A] = True

        if number * 2 <= limit and (number != 0):
            B = number * 2

            for i in range(5):
                D = d[i]
                Q = B // D

                if 0 < Q:
                    B -= D
                    break
            
            if not visited[B]:
                queue.append((B, count + 1))
                visited[B] = True
    
    return -1

N, T, G = map(int, input().split())

C = BFS(N)

if C == -1:
    print('ANG')
else:
    print(C)