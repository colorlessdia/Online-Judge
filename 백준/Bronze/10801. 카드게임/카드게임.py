a = map(int, input().split())
b = map(int, input().split())

a_score = 0
b_score = 0

for aa, bb in zip(a, b):
    if bb < aa:
        a_score += 1
    elif aa < bb:
        b_score += 1

if a_score == b_score:
    print('D')
elif b_score < a_score:
    print('A')
elif a_score < b_score:
    print('B')