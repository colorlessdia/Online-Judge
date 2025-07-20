import sys
from collections import deque

def BFS(N, prime_set):
    queue = deque([(N, 0)])
    limit = (10 ** 6) * 2
    visited = [0] * (limit + 1)
    visited[N] = 1

    while queue:
        number, count = queue.popleft()

        if not (2 <= number <= limit):
            continue

        if number in prime_set:
            return count
        
        d = [number // 2, number // 3, number + 1, number - 1]

        for i in range(4):
            D = d[i]

            if not (2 <= D <= limit):
                continue

            if visited[D]:
                continue

            queue.append((D, count + 1))
            visited[D] = 1
    
    return -1

input = sys.stdin.readline

maximum_number = 10 ** 5

is_prime = [1] * (maximum_number + 1)
is_prime[0] = 0
is_prime[1] = 0

for i in range(2, int(maximum_number ** 0.5) + 1):

    if not is_prime[i]:
        continue

    for j in range(i * i, maximum_number + 1, i):
        is_prime[j] = 0

T = int(input())

for _ in range(T):
    N, A, B = map(int, input().split())

    prime_set = set(i for i in range(A, B + 1) if is_prime[i])

    if not prime_set:
        print(-1)
        continue

    print(BFS(N, prime_set))