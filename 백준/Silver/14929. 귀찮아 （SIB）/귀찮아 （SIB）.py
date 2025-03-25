N = int(input())
X_list = [0] + list(map(int, input().split()))

prefix_sum = [0] * (N + 1)
prefix_square_sum = [0] * (N + 1)

for i in range(1, N + 1):
    X = X_list[i]

    prefix_sum[i] = prefix_sum[i - 1] + X
    prefix_square_sum[i] = prefix_square_sum[i - 1] + (X ** 2)

sum_result = prefix_sum[N] ** 2
square_sum_result = prefix_square_sum[N]

result = (sum_result - square_sum_result) // 2

print(result)