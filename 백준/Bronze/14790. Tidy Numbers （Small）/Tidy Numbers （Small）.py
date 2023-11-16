import sys

for i in range(1, int(input()) + 1):
    n = int(sys.stdin.readline())
    
    for j in reversed(range(1, n + 1)):
        if j == int(''.join(map(str, sorted(map(int, list(str(j))))))):
            print(f'Case #{i}: {j}')
            break