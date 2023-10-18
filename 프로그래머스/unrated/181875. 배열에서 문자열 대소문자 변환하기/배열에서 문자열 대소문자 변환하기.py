def solution(strArr):
    result = []
    
    for i, c in enumerate(strArr):
        if i % 2 == 0:
            result.append(c.lower())
        else:
            result.append(c.upper())
    
    return result
        