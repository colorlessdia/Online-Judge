N, K = map(int, input().split())

mx, mn = max(K, N - K), min(K, N - K)
numerator, denominator = 1, 1

for i in range(mx + 1, N + 1):
    numerator *= i

for j in range(2, mn + 1):
    denominator *= j

print(numerator // denominator)