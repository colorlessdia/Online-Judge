import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    line_A = list(map(int, input().split()))
    line_B = list(map(int, input().split()))

    count_A = [0] * (4 + 1)
    count_B = [0] * (4 + 1)

    for A in line_A[1:]:
        count_A[A] += 1

    for B in line_B[1:]:
        count_B[B] += 1

    score_A = 0
    score_B = 0
    
    for i in range(4, 0, -1):
        A = count_A[i]
        B = count_B[i]

        if A == B:
            continue
        elif B < A:
            score_A += 1
            break
        elif A < B:
            score_B += 1
            break
    
    if A == B:
        print('D')
    elif B < A:
        print('A')
    elif A < B:
        print('B')