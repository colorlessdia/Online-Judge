A, B = map(int, input().split())
q, r = divmod(A, B)

if A != 0 and r < 0:
    q += 1
    r -= B

print(q)
print(r)