import sys

input = sys.stdin.readline

while True:
    N = int(input())

    if N == 0:
        break

    score_count = dict()

    for _ in range(N):
        line = list(map(int, input().split()))
        M, D_list = line[0], line[1:]

        for i, score in enumerate(range(3, 3 - M, -1)):
            D = D_list[i]

            if D not in score_count:
                score_count[D] = [0] * 4
            
            score_count[D][score] += 1
            score_count[D][0] += score
    
    li = sorted(score_count.items(), key=lambda x: (-x[1][0], -x[1][3], -x[1][2]))
    winners = []
    best_score = li[0][1]

    for logo, score in li:
        
        if score == best_score:
            winners.append(logo)
        else:
            break
    
    print(*sorted(winners))