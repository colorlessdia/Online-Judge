import sys

N, K = map(int, sys.stdin.readline().split())
L = N - K - 1

score_list = sorted([float(sys.stdin.readline()) for _ in range(N)])

common_sum = 0

for i in range(N):

    if K <= i <= L:
        common_sum += score_list[i]

adjusted_mean = common_sum / (N - K - K)
trimmed_mean = (common_sum + (score_list[K] * K) + (score_list[L] * K)) / N

adjustement = 0.00000001

print(f'{adjusted_mean + adjustement:.2f}')
print(f'{trimmed_mean + adjustement:.2f}')