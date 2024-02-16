N = int(input())
card_list = list(map(int, input().split()))

group_list = []
temp = []

for card in card_list:
    if len(temp) == 0:
        temp.append(card)
    else:
        if card - temp[-1] == 1:
            temp.append(card)
        else:
            group_list.append(temp)
            temp = [card]

group_list.append(temp)

score = 0

for group in group_list:
    score += group[0]

print(score)