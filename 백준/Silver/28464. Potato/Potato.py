N = int(input())
A = sorted(list(map(int, input().split())))

len_half = len(A) // 2

s = sum(A[:len_half])
p = sum(A[len_half:])

print(s, p)