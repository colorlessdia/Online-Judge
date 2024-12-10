import sys

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break
    
    card_deck = [sys.stdin.readline().rstrip() for _ in range(n)]
    count = len(card_deck)

    half = count // 2 if count % 2 == 0 else (count // 2) + 1

    top_deck = card_deck[:half]
    bot_deck = card_deck[half:]

    shuffle_deck = []

    for i in range(len(bot_deck)):
        shuffle_deck.append(top_deck[i])
        shuffle_deck.append(bot_deck[i])
    
    if count % 2 != 0:
        shuffle_deck.append(top_deck[-1])

    for card in shuffle_deck:
        print(card)