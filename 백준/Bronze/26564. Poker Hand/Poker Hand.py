import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    card_list = input().rstrip().split()

    rank_count = dict(zip(list('A23456789TJQK'), [0] * 13))

    for card in card_list:
        rank = card[0]
        rank_count[rank] += 1
    
    strength = max(rank_count.values())

    print(strength)