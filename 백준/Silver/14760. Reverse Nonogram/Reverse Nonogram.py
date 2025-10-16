import sys

input = sys.stdin.readline

def read_graph_line(graph):

    for line in graph:
        temp = []
        count = 1 if line[0] == 1 else 0
        
        for i in range(1, N):
            current = line[i]

            if current == 1:
                count += 1
                continue

            if 0 < count:
                temp.append(count)
                count = 0

        if 0 < count:
            temp.append(count)
            count = 0

        if len(temp) == 0:
            print(0)
        else:
            print(*temp)

while True:
    N = int(input())

    if N == 0:
        break

    row_graph = [[0 for _ in range(N)] for _ in range(N)]
    col_graph = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        row = input().rstrip()

        for j in range(N):
            col = row[j]

            if col == 'X':
                row_graph[i][j] = 1
                col_graph[j][i] = 1
    
    read_graph_line(row_graph)
    read_graph_line(col_graph)