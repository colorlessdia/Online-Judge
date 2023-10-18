def solution(my_string, indices):
    result = list(my_string)
    
    for i in sorted(indices, key=lambda x: -x):
        result.pop(i)
    
    return ''.join(result)