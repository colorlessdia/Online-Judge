N = int(input())
S = input()

before = ''

joi_string = ''

for char in S:
    if before == '':
        before = char
        joi_string = char
        continue
    
    if char == before:
        joi_string = joi_string[:-1] + joi_string[-1].upper() + char.upper()
        before = char.upper()
    else:
        joi_string += char
        before = char

print(joi_string)