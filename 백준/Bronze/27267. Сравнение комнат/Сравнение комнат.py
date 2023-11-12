a, b, c, d = map(int, input().split())

m = a * b
p = c * d

if m == p:
    print('E')
elif m < p:
    print('P')
elif p < m:
    print('M')