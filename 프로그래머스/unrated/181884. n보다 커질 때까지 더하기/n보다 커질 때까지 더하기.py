def solution(numbers, n):
    total = 0
    
    for num in numbers:
        total += num
        
        if n < total:
            return total