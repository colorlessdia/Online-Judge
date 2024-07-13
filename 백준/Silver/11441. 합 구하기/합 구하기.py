import sys

N = int(sys.stdin.readline())
An = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())

prefix_sum = [0] * (N + 1)

for index, A in enumerate(An, 1):
    prefix_sum[index] = prefix_sum[index - 1] + A

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())

    print(prefix_sum[j] - prefix_sum[i - 1])