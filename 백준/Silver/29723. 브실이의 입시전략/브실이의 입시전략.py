import sys

n, m, k = map(int, input().split())

score_dict = dict()

for _ in range(n):
    subject, score = sys.stdin.readline().rstrip().split()
    score_dict[subject] = int(score)

total_score = 0

for _ in range(k):
    open_subject = sys.stdin.readline().rstrip()
    total_score += score_dict[open_subject]
    del score_dict[open_subject]

diff = m - k

sort_score = sorted(score_dict.values(), key=lambda x: x)

mn_score, mx_score = 0, 0

for i in range(diff):
    mn_score += sort_score[i]
    mx_score += sort_score[-1 * (i + 1)]

print(mn_score + total_score, mx_score + total_score)