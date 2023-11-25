from string import ascii_lowercase, ascii_uppercase

key_alpha = input()
matched_upper = dict(zip(ascii_uppercase, key_alpha.upper()))
matched_lower = dict(zip(ascii_lowercase, key_alpha))
msg = input()

decode = ''

for c in msg:
    if c.isalpha() and c.isupper():
        decode += matched_upper[c]
    elif c.isalpha() and c.islower():
        decode += matched_lower[c]
    else:
        decode += c

print(decode)