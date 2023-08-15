n = int(input())

for i in range(1, n * 2):
    print('*' * i) if i <= n else print('*' * ((n - i) % n))