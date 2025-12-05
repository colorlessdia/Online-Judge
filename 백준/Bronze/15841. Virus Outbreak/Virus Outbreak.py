import sys

input = sys.stdin.readline

dp = [0] * (490 + 1)

for i in range(1, 490 + 1):
    
    if i < 3:
        dp[i] = 1
        continue

    dp[i] = dp[i - 2] + dp[i - 1]

while True:
    H = int(input())

    if H == -1:
        break

    print(f'Hour {H}: {dp[H]} cow(s) affected')