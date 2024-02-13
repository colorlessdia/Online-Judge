import sys

K = int(input())

for i in range(1, K + 1):
    line = list(map(int, sys.stdin.readline().split()))

    N = line[0]
    math_score_list = sorted(line[1:])

    max_score = max(math_score_list)
    min_score = min(math_score_list)
    largest_gap = 0

    for j in range(len(math_score_list) - 1):
        score_gap = math_score_list[j + 1] - math_score_list[j]

        if largest_gap < score_gap:
            largest_gap = score_gap

    print(f'Class {i}')
    print(f'Max {max_score}, Min {min_score}, Largest gap {largest_gap}')