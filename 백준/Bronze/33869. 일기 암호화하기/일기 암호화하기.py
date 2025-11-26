def append_unique_char(char_set, char_list, char):

    if char not in char_set:
        char_set.add(char)
        char_list.append(char)

W = input()
S = input()

char_set = set()
char_list = []

for w in W:
    append_unique_char(char_set, char_list, w)

for i in range(ord('A'), ord('Z') + 1):
    alphabet = chr(i)
    append_unique_char(char_set, char_list, alphabet)

cipher_char_list = []

for s in S:
    index = ord(s) - ord('A')
    cipher_char_list.append(char_list[index])

print(''.join(cipher_char_list))