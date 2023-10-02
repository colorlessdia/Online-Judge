n = int(input())

floor = []

card = [i for i in reversed(range(1, n + 1))]

while 1:
    if len(card) == 1:
        break
    
    floor.append(card[-1])
    card.pop(-1)

    card = card[-1:] + card[:-1]

for f in floor:
    print(f, end=' ')

print(card[0])