import sys
from collections import deque

def BFS(start, end):
    queue = deque([(start, 0)])
    visited = [False] * (10000 + 1)
    visited[start] = True

    d = [1, 10, 100, 1000]

    while queue:
        number, count = queue.popleft()

        if number == end:
            return count

        for i in range(4):
            D = d[i]
            temp = number - (number % (D * 10)) + (number % D)

            for j in range(10):
                n = temp + (D * j)

                if n not in prime_set:
                    continue

                if visited[n]:
                    continue

                queue.append((n, count + 1))
                visited[n] = True
    
    return -1

input = sys.stdin.readline

is_prime = [1] * (10000 + 1)
is_prime[0] = 0
is_prime[1] = 0

for i in range(2, int(10000 ** 0.5) + 1):

    if not is_prime[i]:
        continue

    for j in range(i * i, 10000 + 1, i):
        is_prime[j] = 0

prime_set = set(i for i in range(1000, 10000 + 1) if is_prime[i])

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())

    count = BFS(A, B)

    if 0 <= count:
        print(count)
    else:
        print('Impossible')