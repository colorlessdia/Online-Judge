text = input().upper()

char_count = [0] * 26

for char in text:
    if char.isalpha():
        index = ord(char) - ord('A')

        char_count[index] += 1

for i, count in enumerate(char_count):
    print(chr(i + ord('A')), '|', '*' * count)