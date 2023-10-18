def solution(n):
    result = [n]
    
    while 1:
        if n == 1:
            break
        
        if n % 2 == 0:
            n /= 2
        else:
            n = (3 * n) + 1
            
        result.append(n)
        
    return result