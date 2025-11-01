H = int(input())

H2 = H * 2

for i in range(1, H + 1):
    N = (i * 2) - 1

    if H < N:
        N = (H * 2) - N
    
    N2 = N * 2

    print(f'{'*' * N}{' ' * (H2 - N2)}{'*' * N}')