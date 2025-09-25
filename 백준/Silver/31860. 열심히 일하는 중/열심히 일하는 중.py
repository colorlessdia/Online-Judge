import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N, M, K = map(int, input().split())

maximum_heap = []

for _ in range(N):
    D = int(input())

    heappush(maximum_heap, -D)

Y = 0
S_list = []

while maximum_heap:
    P = -heappop(maximum_heap)

    Y = (Y // 2) + P
    S_list.append(Y)

    P -= M

    if K < P:
        heappush(maximum_heap, -P)

print(len(S_list))

for S in S_list:
    print(S)