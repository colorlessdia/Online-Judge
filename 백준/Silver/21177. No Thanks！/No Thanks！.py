from collections import deque

n = int(input())
card_deck = sorted(map(int, input().split()))

stack = deque()

score = 0

for card in card_deck:
    
    if len(stack) == 0:
        stack.append(card)
        continue
    
    if stack[-1] + 1 == card:
        stack.append(card)
        continue
    
    score += stack[0]

    stack.clear()
    stack.append(card)

if len(stack) != 0:
    score += stack[0]

print(score)