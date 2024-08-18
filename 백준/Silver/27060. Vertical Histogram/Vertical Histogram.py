uppercase_alphabat = [0] * 26

for i, ascii_code in enumerate(range(65, 90 + 1)):
    uppercase_alphabat[i] = chr(ascii_code)

alphabat_count = dict(zip(uppercase_alphabat, [0] * 26))

for _ in range(4):
    line = input()

    for char in line:
        
        if char.isalpha():
            alphabat_count[char] += 1

max_count = max(alphabat_count.values())

bar = ''

for j in reversed(range(1, max_count + 1)):
    
    for alphabat in uppercase_alphabat:
        count = alphabat_count[alphabat]

        if count == j:
            alphabat_count[alphabat] -= 1
            bar += '* '
        else:
            bar += '  '
    
    last_space_index = bar[::-1].index('*')

    print(bar[:-last_space_index])
    
    bar = ''

print(*uppercase_alphabat)