N = int(input())
S_list = sorted(map(int, input().split()))

minimum_G = 200000

for i in range(N):
    G = S_list[i] + S_list[-(i + 1)]

    if G < minimum_G:
        minimum_G = G

print(minimum_G)