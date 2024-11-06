import sys

N = int(sys.stdin.readline())

score_list = [int(sys.stdin.readline()) for _ in range(N)][::-1]

before_score = score_list[0]

count = 0

for i in range(1, N):
    current_score = score_list[i]

    if current_score < before_score:
        before_score = current_score
        continue
    
    difference = current_score - before_score + 1

    before_score = current_score - difference

    count += difference

print(count)