import sys

input = sys.stdin.readline

T = int(input())

for t in range(1, T + 1):
    N = int(input())

    target = None
    is_find = False
    number_set = set()

    if 0 < N:

        for i in range(1, 200 + 1):
            S = str(N * i)

            for j in S:

                if j not in number_set:
                    number_set.add(j)
                
                if len(number_set) == 10:
                    is_find = True
                    break
            
            if is_find:
                target = S
                break

    print(f'Case #{t}: {target if is_find else 'INSOMNIA'}')