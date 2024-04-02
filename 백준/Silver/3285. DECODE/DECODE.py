from string import ascii_uppercase

keyword = input()
K = int(input())
text = input()

alternative_table = ascii_uppercase

for char in keyword:
    alternative_table = alternative_table.replace(char, '')

alternative_table = keyword + alternative_table
alternative_table = alternative_table[-K + 1:] + alternative_table[:-K + 1]

matched_code = dict(zip(list(alternative_table), list(ascii_uppercase)))

decode = ''

for char in text:
    decode += matched_code[char]

print(decode)