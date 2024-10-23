import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    score_list = sorted(map(int, sys.stdin.readline().split()))

    A = (score_list[0] + score_list[-1]) / 2
    B = sum(score_list) / n

    if abs(A - B) < 1:
        print('Yes')
    else:
        print('No')