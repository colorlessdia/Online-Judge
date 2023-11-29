import sys

score = 0
matched_score = dict(zip(['P', 'p', 'N', 'n', 'B', 'b', 'R', 'r', 'Q', 'q'], [1,-1,3,-3,3,-3,5,-5,9,-9]))

for _ in range(8):
    s = sys.stdin.readline().rstrip()
    
    for ss in s:
        if ss in matched_score:
            score += matched_score[ss]

print(score)