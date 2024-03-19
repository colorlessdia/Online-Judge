from collections import deque

N = int(input())

if N == 1:
    print(1)
else:
    card_queue = deque(range(1, N + 1))

    last_card = 0

    while True:
        card_queue.popleft()
        card_queue.append(card_queue.popleft())

        if len(card_queue) == 1:
            last_card = card_queue[0]
            break
        
    print(last_card)