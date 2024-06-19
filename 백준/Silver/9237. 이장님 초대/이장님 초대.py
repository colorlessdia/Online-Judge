N = int(input())
T = sorted(map(int, input().split()), key=lambda x: -x)

invitation_day = 0

for i, t in enumerate(T, 1):
    if invitation_day < i + t + 1:
        invitation_day = i + t + 1

print(invitation_day)