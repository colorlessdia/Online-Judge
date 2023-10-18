def solution(my_strings, parts):
    result = ''
    
    for s, p in zip(my_strings, parts):
        result += s[p[0]:p[1] + 1]
    
    return result
    
    