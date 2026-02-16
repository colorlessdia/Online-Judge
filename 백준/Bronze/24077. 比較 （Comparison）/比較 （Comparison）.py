N, M = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

count = 0

for i in range(N):
    A = A_list[i]

    for j in range(M):
        B = B_list[j]

        if A <= B:
            count += 1

print(count)