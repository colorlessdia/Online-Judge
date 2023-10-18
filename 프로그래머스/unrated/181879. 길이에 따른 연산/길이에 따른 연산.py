def solution(num_list):
    if 11 <= len(num_list):
        return sum(num_list)
    else:
        total = 1
        
        for i in num_list:
            total *= i
    
        return total