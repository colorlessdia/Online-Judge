N, K = map(int, input().split())
A_list = list(map(int, input().split()))

count = 0
is_valid = True

for i in range(1, N):
    before = A_list[i - 1]
    current = A_list[i]

    if before < current:
        continue

    if before < current + K:
        count += 1
        A_list[i] += K
        continue

    is_valid = False
    break

if is_valid:
    print(count)
else:
    print(-1)