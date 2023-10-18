def solution(q, r, code):
    result = ''
    
    for i, c in enumerate(code):
        if i % q == r:
            result += c
    
    return result