K = int(input())
encryption_text = input()

decryption_text = ''

for char in encryption_text:
    if not char.isalpha():
        decryption_text += char
        continue

    index = ord(char) - ord('a') - K

    if 0 <= index:
        decryption_text += chr(ord('a') + index)
    else:
        decryption_text += chr(ord('z') + index + 1)

    K += 1

    if K == 26:
        K = 1

print(decryption_text)