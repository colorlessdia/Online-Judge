import sys

N, Q = map(int, sys.stdin.readline().split())

prefix_sum = [0] * (N + 1)

for i in range(1, N + 1):
    H = int(sys.stdin.readline())

    prefix_sum[i] = prefix_sum[i - 1] + H

for _ in range(Q):
    S, E = map(int, sys.stdin.readline().split())

    count = prefix_sum[E] - prefix_sum[S - 1]

    print(count)