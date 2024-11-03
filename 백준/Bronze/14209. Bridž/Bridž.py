N = int(input())

matched_score = dict(zip(list('JQKA'), list(range(1, 4 + 1))))

total_score = 0

for _ in range(N):
    card_deck = input()

    for card in card_deck:

        if card == 'X':
            continue

        if card.isdigit():
            total_score += int(card)
            continue
      
        total_score += matched_score[card]

print(total_score)