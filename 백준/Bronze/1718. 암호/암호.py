from string import ascii_lowercase

plain_text = input()
encryption_key = input()

lowercase = ascii_lowercase

cryptogram = ''

index = 0

for char in plain_text:
    if char == ' ':
        cryptogram += ' '
    else:
        key = encryption_key[index]
        key_index = ord(key) - ord('a')
        char_index = ord(char) - ord('a')

        cryptogram += lowercase[char_index - key_index - 1]

    if len(encryption_key) - 1 == index:
        index = 0
    else:
        index += 1

print(cryptogram)