import sys

input = sys.stdin.readline

while True:
    N, M, K = map(int, input().split())

    if N == M == K == 0:
        break

    P_list = list(map(int, input().split()))
    total_count = N
    count = N

    for i in range(M - 1):
        P = P_list[i % K]
        count += P
        total_count += count
    
    print(total_count)