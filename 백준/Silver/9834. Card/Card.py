from collections import deque

m, k, s = input().split()
m, k = int(m), int(k)

card_deck = deque(range(m))

for command in s[:-1]:
    
    if command == 'A':
        card_deck.append(card_deck.popleft())
        continue
    
    temp = card_deck.popleft()
    card_deck.append(card_deck.popleft())
    card_deck.appendleft(temp)

print(card_deck[k - 1], card_deck[k], card_deck[k + 1])