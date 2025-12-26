import sys

input = sys.stdin.readline

N = int(input())
A_list = [int(input()) for _ in range(N)]

print(0)

for i in range(1, N):
    A = A_list[i]
    count = 0

    for j in range(i - 1, -1, -1):
        B = A_list[j]

        if B < A:
            count += 1
    
    print(count)