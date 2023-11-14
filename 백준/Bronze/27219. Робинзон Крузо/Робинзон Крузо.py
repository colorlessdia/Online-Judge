check = ''

for i in range(1, int(input()) + 1):
    if i % 5 == 0:
        check = check[:-4] + 'V'
    else:
        check += 'I'

print(check)