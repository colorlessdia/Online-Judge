import sys

N = int(sys.stdin.readline())

score_list = [0] * 76

for _ in range(N):
    score_list[int(sys.stdin.readline())] += 1

tier_count = []
tier_score = []

for i in reversed(range(75 + 1)):
    
    if len(tier_count) == 3:
        break

    if score_list[i] == 0:
        continue
    
    tier_count.append(score_list[i])
    tier_score.append(i)

print(tier_score[-1], tier_count[-1])