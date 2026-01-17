N_sequence = map(int, input().split())

for N in N_sequence:
    size = (N * 2) - 3

    for i in range(1, N):
        side = i - 1
        between = size - (side * 2)

        print(f'{' ' * side}*{' ' * between}*')
    
    print(f'{' ' * (N - 1)}*')