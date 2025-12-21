import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    K = input().rstrip()
    L = len(K)

    print(K)

    for i in range(1, L - 1):
        
        if 0 < i < L - 1:
            print(f'{K[i]}{" " * (L - 2)}{K[L - i - 1]}')
    
    if L == 1:
        continue

    print(K[::-1])