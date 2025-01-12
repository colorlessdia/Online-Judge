import sys

T = int(sys.stdin.readline())

for _ in range(T):
    K, N = sys.stdin.readline().rstrip().split()

    octal = int(N, 8) if max(map(int, N)) < 8 else 0
    decimal = int(N)
    hexadecimal = int(N, 16)
    
    print(f'{K} {octal} {decimal} {hexadecimal}')