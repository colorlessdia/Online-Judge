def solution(myString, pat):
    result = ''
    
    for c in myString:
        if c == 'A':
            result += 'B'
        else:
            result += 'A'
    
    return 1 if pat in result else 0