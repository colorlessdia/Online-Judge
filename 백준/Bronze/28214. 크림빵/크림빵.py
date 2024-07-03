N, K, P = map(int, input().split())
bread_list = list(map(int, input().split()))

basic_bread = 0
count = 0

for i, bread in enumerate(bread_list):
    if bread == 0:
        basic_bread += 1

    if i % K == K - 1:
        if basic_bread < P:
            count += 1

        basic_bread = 0

print(count)