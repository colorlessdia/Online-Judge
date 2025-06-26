import sys

input = sys.stdin.readline

N = int(input())

triangle = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = triangle[0][0]

for i in range(N - 1):
    
    for j in range(i + 1):
        dn = dp[i][j]

        if dp[i + 1][j] < triangle[i + 1][j] + dn:
            dp[i + 1][j] = triangle[i + 1][j] + dn
            
        if dp[i + 1][j + 1] < triangle[i + 1][j + 1] + dn:
            dp[i + 1][j + 1] = triangle[i + 1][j + 1] + dn

print(max(dp[N - 1]))