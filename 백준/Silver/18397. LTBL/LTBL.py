import sys

def parsed_number(string):
    return int(''.join([char for char in string if char.isnumeric()]))

def calc_score(dictionary, team, score):
    board = dictionary[team]
    
    for i in range(6):
        
        if score[i] == 0:
            continue
        
        board[i] += score[i]

input = sys.stdin.readline

T = int(input())

for t in range(1, T + 1):
    M = int(input())

    team_history = dict()

    for _ in range(M):
        line = input().rstrip().split()

        AT, AS = line[0], parsed_number(line[1])
        BT, BS = line[-1], parsed_number(line[-2])

        if AT not in team_history:
            team_history[AT] = [0] * 6

        if BT not in team_history:
            team_history[BT] = [0] * 6

        if AS == BS:
            calc_score(team_history, AT, [1, 0, 1, 0, AS, BS])
            calc_score(team_history, BT, [1, 0, 1, 0, BS, AS])
        elif BS < AS:
            calc_score(team_history, AT, [3, 1, 0, 0, AS, BS])
            calc_score(team_history, BT, [0, 0, 0, 1, BS, AS])
        elif AS < BS:
            calc_score(team_history, BT, [3, 1, 0, 0, BS, AS])
            calc_score(team_history, AT, [0, 0, 0, 1, AS, BS])

    sorted_team_history = sorted(
        team_history.items(), 
        key=lambda x: (x[0], -x[1][0], -x[1][1], -x[1][2], x[1][3], -x[1][4], x[1][5])
    )

    for k, v in sorted_team_history:
        v = ','.join(map(str, v))
        print(f'{k},{v}')

    if t != T:
        print()