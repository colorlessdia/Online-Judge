def solution(arr):
    idx = [i for i, a in enumerate(arr) if a == 2]
    
    if len(idx) == 0:
        return [-1]
    else:
        return arr[idx[0]:idx[-1] + 1]