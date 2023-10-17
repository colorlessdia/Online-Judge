def solution(num_list):
    total_odd, total_even = 0, 0
    
    for i, num in enumerate(num_list):
        if i % 2 != 0:
            total_odd += num
        elif i % 2 == 0:
            total_even += num
    
    if total_odd != total_even:
        return max(total_odd, total_even)
    else:
        return total_odd