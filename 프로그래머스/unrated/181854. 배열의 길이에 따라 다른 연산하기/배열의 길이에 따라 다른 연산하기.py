def solution(arr, n):
    is_odd = True if len(arr) % 2 == 1 else False
    
    result = []
    
    if is_odd:
        for i, num in enumerate(arr):
            if i % 2 == 0:
                result.append(num + n)
            else:
                result.append(num)
    else:
        for i, num in enumerate(arr):
            if i % 2 == 1:
                result.append(num + n)
            else:
                result.append(num)
    return result