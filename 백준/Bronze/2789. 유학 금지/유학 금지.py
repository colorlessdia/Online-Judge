S = input()

char_set = set('CAMBRIDGE')
formatted_string = []

for char in S:

    if char not in char_set:
        formatted_string.append(char)

print(''.join(formatted_string))