n = int(input())

for i in range(1, n + 1):
    if i ** 2 <= 100:
        print('*' * (i ** 2))
    else:
        print(('*' * 100) + '...')