N = int(input())

dp = [1, 2, 3]

for i in range(3, N + 1):
    d = dp[i - 1] + dp[i - 2]
    dp.append(d)

print(dp[N - 1])