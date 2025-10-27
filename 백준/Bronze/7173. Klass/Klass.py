import sys

input = sys.stdin.readline

M, N = map(int, input().split())

graph = [[0 for _ in range(N)] for _ in range(M)]

for i in range(M):
    row = input().rstrip()

    for j in range(N):
        col = int(row[j])
        graph[i][j] = col

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

total_attention = 0

for y in range(M):

    for x in range(N):
        A = graph[y][x]
        student_count = 0
        student_attention = 0

        for k in range(4):
            Y, X = y + dy[k], x + dx[k]

            if not ((0 <= Y < M) and (0 <= X < N)):
                continue

            B = graph[Y][X]
            student_count += 1
            student_attention += abs(A - B)
        
        total_attention += (student_attention / student_count)

print(f'{total_attention:.4f}')