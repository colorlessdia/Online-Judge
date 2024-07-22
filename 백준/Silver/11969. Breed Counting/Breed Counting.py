import sys
import copy

N, Q = map(int, sys.stdin.readline().split())

prefix_sum = [[0 for _ in range(4)] for _ in range(N + 1)]

for i in range(1, N + 1):
    breed = int(sys.stdin.readline())

    breed_count = copy.deepcopy(prefix_sum[i - 1])
    breed_count[breed] += 1

    prefix_sum[i] = breed_count

for _ in range(Q):
    a, b = map(int, sys.stdin.readline().split())

    range_breed = []

    for prev_a, prev_b in zip(prefix_sum[a - 1], prefix_sum[b]):
        range_breed.append(prev_b - prev_a)
    
    print(*range_breed[1:])