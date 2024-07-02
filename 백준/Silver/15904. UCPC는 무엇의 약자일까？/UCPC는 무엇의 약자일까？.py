line = input()

result = ''

for char in line:
    if result == '' and char == 'U':
        result += char
    elif result == 'U' and char == 'C':
        result += char
    elif result == 'UC' and char == 'P':
        result += char
    elif result == 'UCP' and char == 'C':
        result += char

if result == 'UCPC':
    print('I love UCPC')
else:
    print('I hate UCPC')