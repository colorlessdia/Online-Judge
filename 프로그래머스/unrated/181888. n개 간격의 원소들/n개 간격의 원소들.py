def solution(num_list, n):
    result = []
    
    for i, num in enumerate(num_list):
        if i % n == 0:
            result.append(num)
            
    return result