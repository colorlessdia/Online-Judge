import sys

while True:
    card_list = sys.stdin.readline().rstrip().split()

    if card_list[0] == '#':
        break

    cheryl, tania = 0, 0

    for card in card_list[:-1]:
        if card == 'A':
            cheryl += 1
            continue

        if int(card) % 2 == 1:
            cheryl += 1
        else:
            tania += 1

    if cheryl == tania:
        print('Draw')
    elif tania < cheryl:
        print('Cheryl')
    elif cheryl < tania:
        print('Tania')