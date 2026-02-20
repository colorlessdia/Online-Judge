import sys

input = sys.stdin.readline

while True:
    line = input().rstrip()

    if line == '#':
        break

    total = 0

    for i, d in enumerate(reversed(line), 2):
        total += i * int(d)
    
    check_digit = 11 - (total % 11)

    if check_digit == 10:
        print(f'{line} -> Rejected')
    elif check_digit == 11:
        print(f'{line} -> 0')
    else:
        print(f'{line} -> {check_digit}')