def solution(str_list):
    direction = ''
    result = []
    
    for c in str_list:
        if c in list('lr'):
            direction = c
            break
    
    if direction == 'l':
        result = str_list[:str_list.index(c)]
    elif direction == 'r':
        result = str_list[str_list.index(c) + 1:]
    
    return result
        
        