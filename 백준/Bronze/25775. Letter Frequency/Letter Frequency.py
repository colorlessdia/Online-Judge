import sys

n = int(sys.stdin.readline())

alphabat_count = dict()

for _ in range(n):
    word = sys.stdin.readline().rstrip()

    for i, char in enumerate(word, 1):
        char_index = ord(char) - ord('a')

        if i not in alphabat_count:
            alphabat_count[i] = [0] * 26

        alphabat_count[i][char_index] += 1

for k, v in alphabat_count.items():
    max_count = max(v)
    frequency_list = []
    
    for char_code, count in enumerate(v, ord('a')):
        
        if count == 0:
            continue
        
        if count < max_count:
            continue
        
        frequency_list.append(chr(char_code))
    
    formatted_frequency_list = ' '.join(frequency_list)
    
    print(f'{k}: {formatted_frequency_list}')