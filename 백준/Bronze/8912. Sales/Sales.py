import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    A_list = list(map(int, input().split()))

    B_list = [0] * N

    for i in range(1, N):
        A = A_list[i]
        A_1 = A_list[i - 1]

        count = 0

        for j in range(i):
            B = A_list[j]
            
            if B <= A:
                count += 1
        
        B_list[i] = count
    
    print(sum(B_list))