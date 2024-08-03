import sys

while True:
    sentence = sys.stdin.readline().rstrip()

    if sentence == 'END':
        break
    
    alphabat_count = [0] * 26
    is_possible = True

    for char in sentence:
        
        if char == ' ':
            continue

        index = ord(char) - ord('A')

        alphabat_count[index] += 1

        if 1 < alphabat_count[index]:
            is_possible = False
            break
    
    if is_possible:
        print(sentence)