N = int(input())

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
dp[0][0] = 1

t = [0] * (N + 1)
t[0] = 1

for i in range(1, N + 1):
    k = i

    for j in range(i):
        k -= 1
        t[i] += (t[j] * t[k])

print(t[N])