import sys

input = sys.stdin.readline

dp = [[0 for _ in range(30 + 1)] for _ in range(30 + 1)]
dp[1][1] = 1

count_list = [0 for _ in range(30 + 1)]
count_list[1] = 1

for i in range(2, 30 + 1):
    
    for j in range(1, i + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    count_list[i] = sum(dp[i])

while 1:
    N = int(input())

    if N == 0:
        break
    
    print(count_list[N])