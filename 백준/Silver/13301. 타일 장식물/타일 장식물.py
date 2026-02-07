N = int(input())

dp = [0] * (N + 1)

for i in range(1, N + 1):

    if i < 3:
        dp[i] = 1
    else:
        dp[i] = dp[i - 1] + dp[i - 2]

D1 = dp[N]
D2 = dp[N - 1]
C = (D1 * 2) + ((D1 + D2) * 2)

print(C)