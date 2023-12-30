code = list(input())

formatted_char = dict(zip(['a', 'e', 'i', 'o', 's'], ['4', '3', '1', '0', '5']))

print(''.join([formatted_char[c] if c in formatted_char else c for c in code]))