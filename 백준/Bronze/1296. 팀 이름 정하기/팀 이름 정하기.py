import sys

english_name = input()

name_l = english_name.count('L')
name_o = english_name.count('O')
name_v = english_name.count('V')
name_e = english_name.count('E')

N = int(input())

team_name_dict = dict()

for _ in range(N):
    team_name = sys.stdin.readline().rstrip()

    L = team_name.count('L') + name_l
    O = team_name.count('O') + name_o
    V = team_name.count('V') + name_v
    E = team_name.count('E') + name_e

    winning_odds = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100
    
    team_name_dict[team_name] = winning_odds

result = sorted(team_name_dict.items(), key=lambda x: (-x[1], x[0]))[0][0]

print(result)