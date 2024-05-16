IBAN = input()
IBAN = IBAN[4:] + IBAN[:4]

number = ''

for char in IBAN:
    if char.isalpha():
        number += str(ord(char) - ord('A') + 10)
    else:
        number += char

if int(number) % 97 == 1:
    print('correct')
else:
    print('incorrect')