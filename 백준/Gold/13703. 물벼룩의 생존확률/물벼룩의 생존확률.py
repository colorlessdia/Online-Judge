K, N = map(int, input().split())

dp = [[0 for _ in range(K + N + 1)] for _ in range(N + 1)]
dp[0][K] = 1

for i in range(N):

    for j in range(1, K + i + 1):
        
        if dp[i][j] <= 0:
            continue
        
        if 1 <= j - 1:
            dp[i + 1][j - 1] += dp[i][j]
        
        dp[i + 1][j + 1] += dp[i][j]

print(sum(dp[N]))