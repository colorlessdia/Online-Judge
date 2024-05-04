import sys

while True:
    n, m = map(int, sys.stdin.readline().split())

    if n == m == 0:
        break
    
    score_list = [0] * n

    for _ in range(m):
        p_list = map(int, sys.stdin.readline().split())

        for i, p in enumerate(p_list):
            score_list[i] += p
    
    max_score = max(score_list)

    print(max_score)