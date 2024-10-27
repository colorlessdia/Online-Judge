from string import ascii_uppercase as uppercase

n, c = input().split()
ciphertext = input()

alphabat_count = [0] * 26

for char in ciphertext:
    alphabat_count[ord(char) - 65] += 1

max_char_code = alphabat_count.index(max(alphabat_count))
distance = 0

for i in range(25 + 1):
    formatted_char = chr(((max_char_code + i) % 26) + 65)
    
    if formatted_char == c:
        distance = i
        break
    
value_alphabat = list(uppercase)[distance:] + list(uppercase)[:distance]
matched_alphabat = dict(zip(list(uppercase), value_alphabat))

print(''.join([matched_alphabat[char] for char in ciphertext]))