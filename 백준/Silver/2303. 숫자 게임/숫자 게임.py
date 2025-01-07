import sys
from itertools import combinations

N = int(sys.stdin.readline())

winner = 0
maximum_number = 0

for player_number in range(1, N + 1):
    card_list = list(map(int, sys.stdin.readline().split()))

    maximum_last_number = 0

    for card_combination in set(combinations(card_list, 3)):
        last_number = sum(card_combination) % 10

        if maximum_last_number < last_number:
            maximum_last_number = last_number
    
    if maximum_number <= maximum_last_number:
        winner = player_number
        maximum_number = maximum_last_number

print(winner)