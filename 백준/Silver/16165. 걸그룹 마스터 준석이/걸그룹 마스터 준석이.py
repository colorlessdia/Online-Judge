import sys

N, M = map(int, sys.stdin.readline().split())

girl_group_team = dict()
girl_group_member = dict()

for _ in range(N):
    group_name = sys.stdin.readline().rstrip()
    member_count = int(sys.stdin.readline())

    girl_group_team[group_name] = [0] * member_count

    for i in range(member_count):
        member_name = sys.stdin.readline().rstrip()

        girl_group_team[group_name][i] = member_name
        girl_group_member[member_name] = group_name

for _ in range(M):
    quiz = sys.stdin.readline().rstrip()
    quiz_type = int(sys.stdin.readline())

    if quiz_type == 1:
        team_name = girl_group_member[quiz]

        print(team_name)
        continue
    
    member_list = sorted(girl_group_team[quiz])

    for member in member_list:
        print(member)