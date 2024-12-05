import sys

case_number = 1

while True:
    char_1, char_2 = sys.stdin.readline().rstrip().split()

    if char_1 == char_2 == '#':
        break
    
    if case_number != 1:
        print()
    
    print(f'Case {case_number}')

    n = int(sys.stdin.readline())

    for _ in range(n):
        text = sys.stdin.readline().rstrip()

        formatted_text = ''

        for char in text:
            
            if char.lower() in [char_1, char_2]:
                formatted_text += '_'
                continue
            
            formatted_text += char
        
        print(formatted_text)
    
    case_number += 1