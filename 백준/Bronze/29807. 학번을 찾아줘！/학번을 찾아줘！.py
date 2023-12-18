t = int(input())
score = list(map(int, input().split()))
score += (5 - len(score)) * [0]

student_id = 0

if score[0] > score[2]:
    student_id += (score[0] - score[2]) * 508
else:
    student_id += (score[2] - score[0]) * 108

if score[1] > score[3]:
    student_id += (score[1] - score[3]) * 212
else:
    student_id += (score[3] - score[1]) * 305

if score[4] != 0:
    student_id += score[4] * 707

student_id *= 4763

print(student_id)