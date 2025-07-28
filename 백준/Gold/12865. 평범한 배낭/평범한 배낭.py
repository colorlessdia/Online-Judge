import sys

input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

weight_list = [0] * (N + 1)
value_list = [0] * (N + 1)

for i in range(1, N + 1):
    W, V = map(int, input().split())

    weight_list[i] = W
    value_list[i] = V

for i in range(1, N + 1):
    w = weight_list[i]
    v = value_list[i]

    for j in range(1, K + 1):

        if j < w:
            dp[i][j] = dp[i - 1][j]
            continue

        dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w])

print(dp[N][K])