import sys

T = int(sys.stdin.readline())

for _ in range(T):
    C, P = map(int, sys.stdin.readline().split())

    menu = dict()

    for _ in range(C):
        N, S, M, L = sys.stdin.readline().rstrip().split()

        menu[N] = {
            'small': int(S),
            'medium': int(M),
            'large': int(L)
        }

    delivery_fee = int(100 / P)

    for _ in range(P):
        X, Y, Z = sys.stdin.readline().rstrip().split()

        total_fee = menu[Z][Y] + delivery_fee

        if total_fee % 5 == 1:
            total_fee -= 1
        elif total_fee % 5 == 4:
            total_fee += 1
        
        print(f'{X} {total_fee}')