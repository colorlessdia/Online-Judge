import sys

input = sys.stdin.readline

dp = [0] * (45 + 1)

for i in range(45 + 1):
    
    if i < 2:
        dp[i] = 1
        continue

    dp[i] = dp[i - 1] + dp[i - 2]

N = int(input())

for _ in range(N):
    X = int(input())

    print(dp[X])