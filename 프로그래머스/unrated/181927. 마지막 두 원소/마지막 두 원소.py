def solution(num_list):
    n2, n1 = num_list[-2], num_list[-1]
    result = [*num_list]
    
    if n2 < n1:
        result.append(n1 - n2)
    elif n1 <= n2:
        result.append(n1 * 2)
    
    return result