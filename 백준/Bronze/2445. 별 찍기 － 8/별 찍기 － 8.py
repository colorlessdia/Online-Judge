n = int(input())

for i in range(1, n + 1):
    print(f'{"*" * i}{" " * ((n - i) * 2)}{"*" * i}')

for j in reversed(range(1, n)):
    print(f'{"*" * j}{" " * ((n - j) * 2)}{"*" * j}')