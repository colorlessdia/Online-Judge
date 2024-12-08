PIN = input()
pattern_word = input()

base_lower_code = ord('a')
base_upper_code = ord('A')

sum_range_list = []

i = 0

for char in pattern_word:
    pattern_value = ord(char) + 1

    is_extract = False

    if char.islower():
        pattern_value -= base_lower_code
        is_extract = True
    else:
        pattern_value -= base_upper_code

    if is_extract:
        sum_range_list.append((i, i + pattern_value))

    i += pattern_value

if i == len(PIN):
    sum_number = 0
    
    for start, end in sum_range_list:
        sum_number += sum(map(int, PIN[start:end]))
    
    print(sum_number)
else:
    print('non sequitur')