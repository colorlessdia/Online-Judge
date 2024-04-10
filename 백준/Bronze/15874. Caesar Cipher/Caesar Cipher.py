k, length = map(int, input().split())
s = input()

k %= 26

cipher = ''

for char in s:
    if char.isalpha() and char.isupper():
        if ord(char) + k <= ord('Z'):
            cipher += chr(ord(char) + k)
        else:
            cipher += chr(ord('A') + ((ord(char) + k) % ord('Z')) - 1)
    elif char.isalpha() and char.islower():
        if ord(char) + k <= ord('z'):
            cipher += chr(ord(char) + k)
        else:
            cipher += chr(ord('a') + ((ord(char) + k) % ord('z')) - 1)
    else:
        cipher += char

print(cipher)