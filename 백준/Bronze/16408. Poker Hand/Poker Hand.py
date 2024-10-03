hand_cards = input().split()

rank_count = dict(zip(list('A23456789TJQK'), [0] * 14))

for card in hand_cards:
    rank = card[0]

    rank_count[rank] += 1

rank_power = max(rank_count.values())

print(rank_power)