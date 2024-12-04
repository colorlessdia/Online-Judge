import sys

N, M = map(int, sys.stdin.readline().split())

bad_word_dict = dict()

for _ in range(N):
    bad_word = sys.stdin.readline().rstrip()

    bad_word_dict[bad_word] = 1

bad_word_list = list(bad_word_dict.keys())

matched_char = dict(zip(list('01235678'), list('OLZESBTB')))

for _ in range(M):
    plate = sys.stdin.readline().rstrip()

    formatted_plate = ''

    for char in plate:
        
        if char not in list('01235678'):
            formatted_plate += char
            continue
        
        formatted_plate += matched_char[char]
    
    is_valid = True

    for bad_word in bad_word_list:
        
        if bad_word not in formatted_plate:
            continue
        
        is_valid = False
        break
    
    if is_valid:
        print('VALID')
    else:
        print('INVALID')