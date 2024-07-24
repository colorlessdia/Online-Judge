import sys

t = int(sys.stdin.readline())

for case_count in range(1, t + 1):
    empty_line = sys.stdin.readline().rstrip()
    n, q = map(int, sys.stdin.readline().split())
    numbers = map(int, sys.stdin.readline().split())

    prefix_sum = [0] * (n + 1)

    for index, number in enumerate(numbers, 1):
        prefix_sum[index] = prefix_sum[index - 1] + number

    for _ in range(q):
        i, j = map(int, sys.stdin.readline().split())

        print(prefix_sum[j + 1] - prefix_sum[i])
  
    if case_count < t:
        print()