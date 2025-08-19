import sys

input = sys.stdin.readline

N = int(input())

INF = float('inf')
dist = [[0 if i == j else INF for j in range(N + 1)] for i in range(N + 1)]

while 1:
    A, B = map(int, input().split())

    if A == B == -1:
        break

    dist[A][B] = 1
    dist[B][A] = 1

for k in range(1, N + 1):
    
    for i in range(1, N + 1):

        for j in range(1, N + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

minimum_score = INF

for i in range(1, N + 1):
    score = max(dist[i][1:])

    if score < minimum_score:
        minimum_score = score

candidate_list = []
count = 0

for i in range(1, N + 1):

    if max(dist[i][1:]) == minimum_score:
        candidate_list.append(i)
        count += 1

print(minimum_score, count)
print(*candidate_list)