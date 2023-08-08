import sys
while 1:
    n = int(sys.stdin.readline())
    if n == -1: break

    p = [i for i in range(1, n) if n % i == 0]

    if sum(p) == n:
        pp = list(map(str, p))
        print(str(n) + ' = ' + ' + '.join(pp))
    else:
        print(f'{n} is NOT perfect.')