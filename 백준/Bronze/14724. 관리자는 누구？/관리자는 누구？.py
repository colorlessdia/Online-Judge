import sys

team = 'PROBRAIN,GROW,ARGOS,ADMIN,ANT,MOTION,SPG,COMON,ALMIGHTY'.split(',')
t = input()

max_num = 0
max_num_team = ''

for i in range(9):
    scores = map(int, sys.stdin.readline().split())
    
    for score in scores:
        if max_num < score:
            max_num = score
            max_num_team = team[i]

print(max_num_team)