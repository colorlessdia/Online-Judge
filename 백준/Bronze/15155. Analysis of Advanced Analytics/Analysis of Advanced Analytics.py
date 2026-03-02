N, K = map(int, input().split())
P_list = list(map(int, input().split()))

k = K
count = 1

for P in P_list:

    if P <= k:
        k -= P
    else:
        k = K - P
        count += 1

print(count)