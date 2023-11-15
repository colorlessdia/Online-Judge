s = input()

b, c = 0, 0

for ss in s:
    if ss == 'B':
        b += 1
    else:
        c += 1

bb = b // 2
cc = c // 2

print(bb + cc)