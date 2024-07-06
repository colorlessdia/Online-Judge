import sys

n = int(sys.stdin.readline())
number_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

prefix_sum = list(range(n + 1))

for i, number in enumerate(number_list, 1):
    prefix_sum[i] = prefix_sum[i - 1] + number

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())

    print(prefix_sum[end + 1] - prefix_sum[start])