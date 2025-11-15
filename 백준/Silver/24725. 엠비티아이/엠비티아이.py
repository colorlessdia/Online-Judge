import sys

input = sys.stdin.readline

N, M = map(int, input().split())

MBTI_set = set()

for i in ['I', 'E']:

    for j in ['N', 'S']:

        for k in ['F', 'T']:

            for l in ['J', 'P']:
                MBTI = ''.join([i, j, k ,l])
                MBTI_set.add(MBTI)

coordinates = [[] for _ in range(8)]

for i in range(4):
    coordinates[0].append((0, i))
    coordinates[1].append((i, i))
    coordinates[2].append((i, 0))
    coordinates[3].append((i, -i))
    coordinates[4].append((0, -i))
    coordinates[5].append((-i, -i))
    coordinates[6].append((-i, 0))
    coordinates[7].append((-i, i))

graph = [input().rstrip() for _ in range(N)]
first_char_set = set(['I', 'E'])
MBTI_char_set = set(['I', 'E', 'N', 'S', 'F', 'T', 'J', 'P'])
MBTI_count = 0

for i in range(N):

    for j in range(M):
        alphabet = graph[i][j]

        if alphabet not in first_char_set:
            continue

        for k in range(8):
            temp = []
            
            for dx, dy in coordinates[k]:
                x = j + dx
                y = i + dy

                if not ((0 <= y < N) and (0 <= x < M)):
                    break

                if graph[y][x] not in MBTI_char_set:
                    break

                temp.append(graph[y][x])

            if len(temp) != 4:
                continue

            string = ''.join(temp)

            if string in MBTI_set:
                MBTI_count += 1

print(MBTI_count)