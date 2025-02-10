from heapq import heapify, heappush, heappop

n, m = map(int, input().split())
card_list = list(map(int, input().split()))

heapify(card_list)

for _ in range(m):
    card_1 = heappop(card_list)
    card_2 = heappop(card_list)

    sum_card_number = card_1 + card_2

    heappush(card_list, sum_card_number)
    heappush(card_list, sum_card_number)

total_card_number = sum(card_list)

print(total_card_number)