import sys

def decimal_to_base(decimal, base):

    if base == 10:
        return str(decimal)
    
    matched_string = '0123456789ABCDEFGHIJ'
    formatted_base = ''

    while 0 < decimal:
        rest = decimal % base
        formatted_base = matched_string[rest] + formatted_base
        decimal //= base
    
    return formatted_base

input = sys.stdin.readline

while 1:
    creature = input().rstrip()

    if creature == '#':
        break
    
    base = int(input())
    decimal = int(input())

    formatted_number = decimal_to_base(decimal, base)

    print(f'{creature}, {decimal}, {formatted_number}')