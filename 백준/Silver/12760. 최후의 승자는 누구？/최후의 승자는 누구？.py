import sys

N, M = map(int, sys.stdin.readline().split())

player_history = dict()
maximun_card_list = [0] * M

for i in range(1, N + 1):
    card_list = sorted(map(int, sys.stdin.readline().split()), key=lambda x: -x)

    player_history[i] = {
        'score': 0,
        'card_list': card_list
    }

    for j in range(M):
        
        if maximun_card_list[j] < card_list[j]:
            maximun_card_list[j] = card_list[j]

maximun_score = 0

for player, v in player_history.items():
    
    for k in range(M):
        
        if maximun_card_list[k] != v['card_list'][k]:
            continue
        
        player_history[player]['score'] += 1

        if maximun_score < player_history[player]['score']:
            maximun_score = player_history[player]['score']

best_player_list = []

for player, v in player_history.items():
    
    if maximun_score == v['score']:
        best_player_list.append(str(player))

print(' '.join(best_player_list))