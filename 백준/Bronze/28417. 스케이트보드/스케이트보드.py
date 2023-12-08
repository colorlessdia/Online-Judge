import sys

max_score = 0

for _ in range(int(input())):
    s = sys.stdin.readline().rstrip().split()
    score = max(list(map(int, s[:2]))) + sum(sorted(list(map(int, s[2:])))[-2:])

    if max_score < score:
        max_score = score

print(max_score)