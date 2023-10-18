def solution(my_string, m, c):
    result = []
    temp = ''
    
    for i, s in enumerate(my_string, 1):
        if i % m != 0:
            temp += s
        else:
            temp += s
            result.append(temp[c - 1])
            temp = ''
    
    return ''.join(result)