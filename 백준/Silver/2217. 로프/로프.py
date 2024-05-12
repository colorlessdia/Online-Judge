import sys

N = int(sys.stdin.readline())
rope_list = [int(sys.stdin.readline()) for _ in range(N)]

max_weight = 0
k = 1

for rope in sorted(rope_list, reverse=True):
    weight = rope * k

    if max_weight < weight:
        max_weight = weight

    k += 1

print(max_weight)