import sys
import heapq as hq

input = sys.stdin.readline

heap = []

N = int(input())

for _ in range(N):
    size = int(input())

    hq.heappush(heap, size)

count = 0

while 1 < len(heap):
    A = hq.heappop(heap)
    B = hq.heappop(heap)

    count += A + B

    hq.heappush(heap, A + B)

print(count)