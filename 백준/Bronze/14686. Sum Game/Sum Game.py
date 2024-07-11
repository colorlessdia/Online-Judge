N = int(input())

swifts_scores = [0] + list(map(int, input().split()))
semaphores_scores = [0] + list(map(int, input().split()))

swifts_prefix_sum = list(range(N + 1))
semaphores_prefix_sum = list(range(N + 1))

K = 0

for i in range(1, N + 1):
    swifts_prefix_sum[i] = swifts_prefix_sum[i - 1] + swifts_scores[i]
    semaphores_prefix_sum[i] = semaphores_prefix_sum[i - 1] + semaphores_scores[i]

    if swifts_prefix_sum[i] == semaphores_prefix_sum[i]:
        K = i

print(K)