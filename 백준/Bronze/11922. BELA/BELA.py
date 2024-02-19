import sys

matched_score_dict = dict(zip(list('AKQJT987'), [[11, 11], [4, 4], [3, 3], [20, 2], [10, 10], [14, 0], [0, 0], [0, 0]]))

N, B = input().split()

score = 0

for _ in range(4 * int(N)):
    K = sys.stdin.readline().rstrip()

    label, shape = K[0], K[1]

    if shape == B:
        score += matched_score_dict[label][0]
    else:
        score += matched_score_dict[label][1]

print(score)