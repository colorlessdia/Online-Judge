import sys

K = 'AHIMTUVWXY18E3JLO0S2Z5'
V = 'AHIMTUVWXY18EEJJOOSSZZ'

matched_char = dict(zip(K, V))

is_first = True

while 1:
    S = sys.stdin.readline().rstrip()

    if S == '':
        break
    
    message = ''

    if S == S[::-1]:
        is_mirrored = all([1 if c in matched_char else 0 for c in S])
        
        if is_mirrored:
            message = 'is a mirrored palindrome.'
        else:
            message = 'is a palindrome.'
    else:
        formatted_S = [matched_char[c] if c in matched_char else c for c in S]
        
        if formatted_S == formatted_S[::-1]:
            message = 'is a mirrored string.'
        else:
            message = 'is not a palindrome.'

    if not is_first:
        print()

    print(f'{S} -- {message}')

    is_first = False