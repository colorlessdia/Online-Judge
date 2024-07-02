N, K, P = map(int, input().split())
bread_list = list(map(int, input().split()))

count = 0

for i in range(0, N * K, K):
    cream_bread = sum(bread_list[i:i + K])

    if P <= cream_bread:
        count += 1

print(count)