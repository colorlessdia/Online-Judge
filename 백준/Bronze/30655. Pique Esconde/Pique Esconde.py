import sys

input = sys.stdin.readline

while True:
    N, M = map(int, input().split())

    if N == M == 0:
        break

    number_set = set([i for i in range(1, N + 1)])
    number_set.remove(M)

    for i in range(N - 2):
        m = int(input())

        number_set.remove(m)
    
    print(*number_set)