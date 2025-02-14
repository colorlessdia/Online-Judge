N = int(input())

for i in range(1, N + 1):
    line = (' *' * N) if i % 2 == 0 else ('* ' * N)[:-1]

    print(line)