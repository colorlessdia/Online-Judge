S = input()

uppercase = ''.join([chr(i) for i in range(ord('A'), ord('Z') + 1)])
negative_char = uppercase[13:] + uppercase[:13]

matched_nagative = dict(zip(uppercase, negative_char))

before_char = 'A'

time = 0

for char in S:
    
    if char == matched_nagative[before_char]:
        time += 13
    elif char != before_char:
        i = uppercase.index(before_char)

        alphabat_list = uppercase[i:] + uppercase[:i]

        right = alphabat_list[1:13]
        left = alphabat_list[14:][::-1]

        for t, items in enumerate(zip(right, left), 1):
            
            if char in items:
                time += t
                break
    
    before_char = char

print(time)