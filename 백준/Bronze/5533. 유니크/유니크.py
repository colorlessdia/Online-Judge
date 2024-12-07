import sys

N = int(sys.stdin.readline())

player_score_list = [[] for _ in range(N)]

round_score_count = dict(zip([1, 2, 3], [{} for _ in range(3)]))

for i in range(N):
    score_list = list(map(int, sys.stdin.readline().split()))

    player_score_list[i] = score_list

    for j in range(3):
        score = score_list[j]
        round = j + 1

        if score not in round_score_count[round]:
            round_score_count[round][score] = 1
            continue
        
        round_score_count[round][score] += 1

for player_score in player_score_list:
    total_score = 0
    
    for k in range(3):
        score = player_score[k]
        round = k + 1
        
        if round_score_count[round][score] == 1:
            total_score += score

    print(total_score)