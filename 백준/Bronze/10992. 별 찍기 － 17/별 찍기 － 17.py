N = int(input())

for i in range(1, N + 1):
    
    if i == 1:
        print(f'{' ' * (N - 1)}*')
    elif i < N:
        print(f'{' ' * (N - i)}*{' ' * (((i - 1) * 2) - 1)}*')
    else:
        print(f'{'*' * ((N * 2) - 1)}')