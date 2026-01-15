import sys

input = sys.stdin.readline

T = int(input())

char_set = set('aeiou')

for t in range(1, T + 1):
    S = input().rstrip()
    C = S[-1]
    R = 'nobody'

    if C in char_set:
        R = 'a queen'
    elif C != 'y':
        R = 'a king'

    print(f'Case #{t}: {S} is ruled by {R}.')