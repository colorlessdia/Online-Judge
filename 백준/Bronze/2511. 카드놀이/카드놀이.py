A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_score = 0
B_score = 0

last_winner = None

for a, b in zip(A_list, B_list):
    if a == b:
        A_score += 1
        B_score += 1
    elif b < a:
        A_score += 3
        last_winner = 'A'
    elif a < b:
        B_score += 3
        last_winner = 'B'

print(A_score, B_score)

if A_score == B_score and last_winner != None:
    print(last_winner)
elif A_score == B_score:
    print('D')
elif B_score < A_score:
    print('A')
elif A_score < B_score:
    print('B')