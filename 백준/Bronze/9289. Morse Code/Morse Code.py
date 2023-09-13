import sys
import string

upper_alpha = string.ascii_uppercase
morse = ('.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..').split()

morse_dict = dict(zip(morse, upper_alpha))

for i in range(1, int(input()) + 1):
    s = sys.stdin.readline().rstrip().split()

    word = ''

    for ss in s:
        word += morse_dict[ss]
    
    print(f'Case {i}: {word}')