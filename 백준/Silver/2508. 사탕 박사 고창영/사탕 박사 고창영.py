import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    _ = input()
    R, C = map(int, input().split())

    graph = [['' for _ in range(C + 2)] for _ in range(R + 2)]
    candy_list = []

    for i in range(1, R + 1):
        row = input().rstrip()

        for j in range(1, C + 1):
            col = row[j - 1]
            graph[i][j] = col

            if col == 'o':
                candy_list.append((i, j))
    
    count = 0

    for y, x in candy_list:
        row = (graph[y][x - 1] == '>') and (graph[y][x + 1] == '<')
        col = (graph[y - 1][x] == 'v') and (graph[y + 1][x] == '^')

        if row or col:
            count += 1
    
    print(count)