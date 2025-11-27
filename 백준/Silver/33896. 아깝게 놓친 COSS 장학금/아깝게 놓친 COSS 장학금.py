import sys

input = sys.stdin.readline

N = int(input())

scholarship_score_list = []

for _ in range(N):
    line = input().rstrip().split()
    name = line[0]
    score, risk, cost = map(int, line[1:])

    scholarship_score = int((score ** 3) / (cost * (risk + 1)))
    scholarship_score_list.append((name, scholarship_score, cost))

scholarship_score_list.sort(key=lambda x: (-x[1], x[2], x[0]))
scholarship_student = scholarship_score_list[1][0]

print(scholarship_student)