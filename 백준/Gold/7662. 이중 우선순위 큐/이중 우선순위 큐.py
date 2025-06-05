import sys
from heapq import heappush, heappop

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())

    AQ = []
    DQ = []
    check_number = {}

    for _ in range(K):
        C, N = input().rstrip().split()
        N = int(N)

        if C == 'I':
            heappush(AQ, N)
            heappush(DQ, -N)
            check_number[N] = check_number.get(N, 0) + 1
            continue
        
        if N == -1:
            
            while AQ:
                AN = heappop(AQ)

                if 0 < check_number[AN]:
                    check_number[AN] -= 1
                    break
                
            continue
        
        if N == 1:
            
            while DQ:
                DN = -heappop(DQ)

                if 0 < check_number[DN]:
                    check_number[DN] -= 1
                    break
                
            continue
    
    min_number = None

    while AQ:
        AN = heappop(AQ)

        if 0 < check_number[AN]:
            min_number = AN
            break
    
    max_number = None

    while DQ:
        DN = -heappop(DQ)

        if 0 < check_number[DN]:
            max_number = DN
            break

    if min_number == max_number == None:
        print('EMPTY')
    else:
        print(max_number, min_number)