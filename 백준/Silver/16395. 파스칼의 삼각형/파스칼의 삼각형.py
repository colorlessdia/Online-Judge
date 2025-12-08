def is_one(r, c):

    if (r == c) or (c == 0):
        return 1

    return 0

N, K = map(int, input().split())

dp = [[is_one(i, j) for j in range(N)] for i in range(N)]

for i in range(2, N):
    
    for j in range(1, i):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

print(dp[N - 1][K - 1])