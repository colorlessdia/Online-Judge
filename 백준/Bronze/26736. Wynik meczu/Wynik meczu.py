s = input()

a, b = 0, 0

for ss in s:
    if ss == 'A':
        a += 1
    else:
        b += 1

print(f'{a} : {b}')