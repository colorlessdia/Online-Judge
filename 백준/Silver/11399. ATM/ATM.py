N = int(input())
P = map(int, input().split())

mapped_withdraw = dict(zip(range(1, N + 1), P))
sorted_withdraw = sorted(mapped_withdraw.values())

prefix_sum = [0] * (N + 1)

for i, withdraw_time in enumerate(sorted_withdraw, 1):
    prefix_sum[i] = prefix_sum[i - 1] + withdraw_time

print(sum(prefix_sum))