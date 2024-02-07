import sys

n = int(input())

for i in range(1, n + 1):
    a, b, c = sorted(list(map(int, sys.stdin.readline().split())))

    print(f'Scenario #{i}:')

    if (a ** 2) + (b ** 2) == c ** 2:
        print('yes')
    else:
        print('no')

    print()