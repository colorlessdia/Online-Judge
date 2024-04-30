ciphertext = input()

integer_set = set()

temp = ''

for i, char in enumerate(ciphertext):
    if char.isdigit():
        temp += char
    elif char.isalpha() and len(temp) != 0:
        integer_set.add(temp)
        temp = ''
    elif char.isalpha():
        temp = ''

    if i == len(ciphertext) - 1 and len(temp) != 0:
        integer_set.add(temp)

print(len(integer_set))