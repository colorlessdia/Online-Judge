import sys

T = int(sys.stdin.readline())

for t in range(1, T + 1):
    country = sys.stdin.readline().rstrip()

    last_char = country[-1].lower()

    ruler = ''

    if last_char == 'y':
        ruler = 'nobody'
    elif last_char in 'aeiou':
        ruler = 'a queen'
    else:
        ruler = 'a king'

    print(f'Case #{t}: {country} is ruled by {ruler}.')