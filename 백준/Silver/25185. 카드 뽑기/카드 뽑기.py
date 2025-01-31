import sys

def is_two_pair(deck):
    
    return all([deck.count(card) in [2, 4] for card in deck])

def is_triple(deck):
    
    return any([1 if 3 <= deck.count(card) else 0 for card in deck])

def is_straight(deck):
    is_valid = False
    
    for card in deck:
        number, alphabat = int(card[0]), card[1]

        if is_valid:
            return 1

        for i in range(number - 2, number + 1):
            temp = []
            
            if i < 1:
                continue
            
            for j in range(i, i + 3):
                
                if 9 < j:
                    continue
                
                if str(j) + alphabat in deck:
                    temp.append(1)
            
            if len(temp) == 3:
                is_valid = True
                break
            
    return 0

T = int(sys.stdin.readline())

for _ in range(T):
    deck = sys.stdin.readline().rstrip().split()

    is_holiday = any([is_two_pair(deck), is_triple(deck), is_straight(deck)])

    if is_holiday:
        print(':)')
    else:
        print(':(')