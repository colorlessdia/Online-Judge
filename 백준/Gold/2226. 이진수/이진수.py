N = int(input())

dp = [0, 0, 1, 1] + ([0] * (N - 3))

for i in range(4, N + 1):
    dp[i] = dp[i - 1] * 2

    if i % 2 == 0:
        dp[i] += 1
    else:
        dp[i] -= 1

print(dp[N])