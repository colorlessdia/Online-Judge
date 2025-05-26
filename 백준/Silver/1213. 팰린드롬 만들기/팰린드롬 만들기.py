S = input()

if len(S) == 1:
    print(S)
else:
    char_count = dict()

    for char in S:
        
        if char not in char_count:
            char_count[char] = 1
            continue
        
        char_count[char] += 1
    
    values = char_count.values()

    is_even = 1 if len(S) % 2 == 0 else 0
    is_palindrome = False
    
    if is_even:
        is_palindrome = all([1 if v % 2 == 0 else 0 for v in values])
    else:
        is_palindrome = 1 if sum([1 for v in values if v % 2 == 1]) == 1 else 0
    
    if is_palindrome:
        part = []
        middle_char = ''
        
        for k, v in sorted(char_count.items(), key=lambda x: x[0]):
            
            while 0 < v:
                
                if v == 1:
                    middle_char = k
                    break
                
                part.append(k)
                v -= 2

        print(''.join(part + [middle_char] + part[::-1]))
    else:
        print('I\'m Sorry Hansoo')