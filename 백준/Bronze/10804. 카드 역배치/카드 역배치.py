card_list = list(range(20 + 1))

for _ in range(10):
    a, b = map(int, input().split())

    card_list = card_list[:a] + card_list[a:b + 1][::-1] + card_list[b + 1:]

print(*card_list[1:])