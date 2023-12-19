n, k = map(int, input().split())
g = list(map(int, input().split()))

d = ''

for gg in g:
    p = gg * 100 // n

    if 0 <= p <= 4:
        d += '1'
    elif 4 < p <= 11:
        d += '2'
    elif 11 < p <= 23:
        d += '3'
    elif 23 < p <= 40:
        d += '4'
    elif 40 < p <= 60:
        d += '5'
    elif 60 < p <= 77:
        d += '6'
    elif 77 < p <= 89:
        d += '7'
    elif 89 < p <= 96:
        d += '8'
    elif 96 < p <= 100:
        d += '9'

print(*list(map(int, list(d))))