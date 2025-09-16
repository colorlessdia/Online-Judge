import sys
from heapq import heappush, heappop

input = sys.stdin.readline

def formatted_time(time):
    hh, mm = map(int, time.split(':'))
    
    return (hh * 60) + mm

N = int(input())

for n in range(1, N + 1):
    T = int(input())
    NA, NB = map(int, input().split())

    schedule = []

    for _ in range(NA):
        s, e = map(formatted_time, input().rstrip().split())
    
        schedule.append((s, e, 'A'))

    for _ in range(NB):
        s, e = map(formatted_time, input().rstrip().split())
    
        schedule.append((s, e, 'B'))

    schedule.sort(key=lambda x: x[0])

    A_pq = []
    B_pq = []

    A_count = 0
    B_count = 0

    for s, e, o in schedule:
        
        if o == 'A':

            if A_pq and (A_pq[0] <= s):
                heappop(A_pq)
            else:
                A_count += 1

            heappush(B_pq, e + T)
            continue

        if o == 'B':

            if B_pq and (B_pq[0] <= s):
                heappop(B_pq)
            else:
                B_count += 1
            
            heappush(A_pq, e + T)
            continue

    print(f'Case #{n}: {A_count} {B_count}')