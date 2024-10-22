import sys
from collections import deque

N, K, P = map(int, sys.stdin.readline().split())

card_deck = deque(range(1, K + 1))
card_stack = deque()

turn = 1

while True:
    current_card = card_deck.popleft()
    
    if N < turn:
        turn = 1

    if turn == N:
        card_stack.append(current_card)
    
    turn += 1
    
    if len(card_deck) == 0:
        break

    for _ in range(P):
        card_deck.append(card_deck.popleft())

for order in sorted(card_stack):
    print(order)