S = input()

L = list('qwertyasdfgzxcvb')
R = list('uiophjklnm')

left_key_count = 0
right_key_count = 0
special_key_count = 0

for s in S:
    char = s

    if char == ' ':
        special_key_count += 1
        continue
    
    if char.isupper():
        special_key_count += 1
        char = char.lower()
    
    if char in L:
        left_key_count += 1
    elif char in R:
        right_key_count += 1

while 0 < special_key_count:
    
    if left_key_count <= right_key_count:
        left_key_count += 1
    else:
        right_key_count += 1
    
    special_key_count -= 1

print(left_key_count, right_key_count)