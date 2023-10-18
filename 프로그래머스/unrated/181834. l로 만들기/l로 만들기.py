def solution(myString):
    result = ''
    
    for c in myString:
        if c < 'l':
            result += 'l'
        else:
            result += c
    
    return result