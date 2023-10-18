def solution(arr, idx):
    result = [i for i, n in enumerate(arr) if idx <= i and n == 1]
    
    return -1 if len(result) == 0 else result[0]