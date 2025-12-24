import sys

input = sys.stdin.readline

N, M, X = map(int, input().split())
H_list = list(map(int, input().split()))

for i in range(N - 1, -1, -1):
    line = ['.' for _ in range(M)]

    for j in range(M):
        H = H_list[j] - 1

        if (i == (X - 1)) and (H < (X - 1)):
            line[j] = '-'
        elif i == (X - 1):
            line[j] = '*'
        elif ((j + 1) % 3 == 0) and (H < i < (X - 1)):
            line[j] = '|'
        elif i <= H:
            line[j] = '#'

    print(''.join(line))