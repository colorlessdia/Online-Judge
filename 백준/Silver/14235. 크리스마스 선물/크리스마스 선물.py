import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())

gift_list = []

for _ in range(N):
    line = list(map(int, input().split()))

    if line[0] == 0:
        
        if len(gift_list) == 0:
            print(-1)
            continue
        
        gift = -heappop(gift_list)

        print(gift)
        continue
    
    for gift in line[1:]:
        heappush(gift_list, -gift)