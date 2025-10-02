import sys

input = sys.stdin.readline

dice_list = []

for i in range(3, 6 + 1):

    for j in range(1, i):
        dice_list.append(''.join([str(i), str(j)]))

dice_list.extend(['11', '22', '33', '44', '55', '66', '21'])
matched_score = dict(zip(dice_list, range(len(dice_list))))

while True:
    a1, a2, b1, b2 = input().rstrip().split()

    if a1 == a2 == b1 == b2 == '0':
        break

    A = matched_score[''.join(sorted([a1, a2], reverse=True))]
    B = matched_score[''.join(sorted([b1, b2], reverse=True))]

    if A == B:
        print('Tie.')
    elif B < A:
        print('Player 1 wins.')
    elif A < B:
        print('Player 2 wins.')