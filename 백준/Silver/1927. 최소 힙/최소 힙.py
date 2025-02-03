import sys
import heapq as hq

input = sys.stdin.readline

heap = []

N = int(input())

for _ in range(N):
    x = int(input())

    if 0 < x:
        hq.heappush(heap, x)
        continue
    
    if len(heap) != 0:
        pop_item = hq.heappop(heap)

        print(pop_item)
        continue
    
    print(0)