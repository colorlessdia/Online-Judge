def solution(arr):
    n = len(arr)
    
    t = sum([1 for i in range(n) for j in range(n) if arr[i][j] == arr[j][i]])
    
    return 1 if n * n == t else 0