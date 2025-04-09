string = input()

lowercase = [chr(l) for l in range(ord('a'), ord('z') + 1)]
uppercase = [chr(u) for u in range(ord('A'), ord('Z') + 1)]
k = lowercase + uppercase
v = [str(i).rjust(2, '0') for i in range(1, 52 + 1)]
matched_char_code = dict(zip(k, v))

encryption_string = ''

for char in string:

    if char.isdigit():
        encryption_string += '#' + char
        continue
    
    if char.isalpha():
        encryption_string += matched_char_code[char]
        continue
    
    encryption_string += char

print(encryption_string)