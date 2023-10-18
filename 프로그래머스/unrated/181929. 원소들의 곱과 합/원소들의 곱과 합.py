def solution(num_list):
    total_mul = 1
    total_sum = sum(num_list) ** 2
    
    for i in num_list:
        total_mul *= i
        
    return 1 if total_mul < total_sum else 0