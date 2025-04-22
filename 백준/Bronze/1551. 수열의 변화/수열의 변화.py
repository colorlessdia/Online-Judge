N, K = map(int, input().split())
A_list = list(map(int, input().split(',')))

for _ in range(K):
    B_list = [0] * (N - 1)

    for i in range(N - 1):
        B_list[i] = A_list[i + 1] - A_list[i]
    
    A_list = B_list
    N -= 1

print(','.join(map(str, A_list)))