number = ''.join([input() for _ in range(4)])

if number[0] in '89' and number[-1] in '89' and number[1] == number[2]:
    print('ignore')
else:
    print('answer')