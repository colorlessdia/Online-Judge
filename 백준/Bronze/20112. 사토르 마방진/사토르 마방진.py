import sys

input = sys.stdin.readline

N = int(input())

graph = [input().rstrip() for _ in range(N)]

is_valid = True

for i in range(N):

    if not is_valid:
        break

    for j in range(N):
        
        if graph[i][j] != graph[j][i]:
            is_valid = False
            break

if is_valid:
    print('YES')
else:
    print('NO')