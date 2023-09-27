import sys

score_list = [list(map(int, sys.stdin.readline().split())) for _ in range(int(input()))]
sort_score = sorted(score_list, key=lambda x: -x[2])

nation_list = []
medal_list = []

for nation, student, score in sort_score:
    if nation_list.count(nation) < 2:
        medal_list.append([nation, student])
        nation_list.append(nation)

for medal in medal_list[:3]:
    print(*medal)