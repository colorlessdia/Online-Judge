import sys
from heapq import heappush, heappop

input = sys.stdin.readline

H = int(input())
N, Q = map(int, input().split())
D_sequence = map(int, input().split())

D_list = []
count = 0
total_D = 0

for D in D_sequence:
    heappush(D_list, D)

    count += 1
    total_D += D

if H <= total_D:
    
    while 1:
        D = heappop(D_list)

        if total_D - D < H:
            heappush(D_list, D)
            break
        
        count -= 1
        total_D -= D
    
    print(count)
else:
    print(-1)

for _ in range(Q):
    card = int(input())
    
    heappush(D_list, card)

    count += 1
    total_D += card

    if total_D < H:
        print(-1)
        continue

    while 1:
        D = heappop(D_list)

        if total_D - D < H:
            heappush(D_list, D)
            break
        
        count -= 1
        total_D -= D
    
    print(count)