import sys

answer = [((i - 1) % 5) + 1 for i in range(1, 10 + 1)]

cnt_list = []

for j in range(1, int(input()) + 1):
    scores = map(int, sys.stdin.readline().split())
    
    score = 0
    
    for s, a in zip(scores, answer):
        if s == a:
            score += 1
    
    if score == 10:
        cnt_list.append(j)

for student in cnt_list:
    print(student)