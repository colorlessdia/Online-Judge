import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    line = list(map(int, input().split()))
    K, N_list = line[0], [0] + line[1:]

    is_fibonacci = True

    if 2 < K:

        for i in range(3, K + 1):
            N1 = N_list[i]
            N2 = N_list[i - 1] + N_list[i - 2]

            if N1 != N2:
                is_fibonacci = False
                break
    
    if is_fibonacci:
        print('YES')
    else:
        print('NO')