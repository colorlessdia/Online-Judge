import sys

input = sys.stdin.readline

N, M = map(int, input().split())

row_set = set()
col_set = set()

for i in range(N):
    row = input().rstrip()

    for j in range(M):
        col = row[j]

        if col == 'X':
            row_set.add(i)
            col_set.add(j)

R = N - len(row_set)
C = M - len(col_set)

print(max(R, C))