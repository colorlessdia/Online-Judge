import sys

input = sys.stdin.readline

T = int(input())

for t in range(1, T + 1):
    R, C = map(int, input().split())
    c = C - 1

    print(f'Case #{t}:')

    print(f'..+{'-+' * c}')
    print(f'..|{'.|' * c}')
    print(f'+-+{'-+' * c}')

    for _ in range(R - 1):
        print(f'|.|{'.|' * c}')
        print(f'+-+{'-+' * c}')