import sys

for _ in range(int(input())):
    card = sys.stdin.readline().rstrip()
    
    card_num = ''
    
    for i, n in enumerate(card[::-1], 1):
        if i % 2 == 0:
            multi_num = int(n) * 2
            
            if 9 < multi_num:
                card_num += str(sum(map(int, list(str(multi_num)))))
            else:
                card_num += str(multi_num)
        else:
            card_num += n

    is_valid = True if sum(map(int, list(card_num))) % 10 == 0 else False

    if is_valid:
        print('T')
    else:
        print('F')