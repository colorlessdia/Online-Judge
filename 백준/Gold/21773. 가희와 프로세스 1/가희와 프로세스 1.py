import sys
from heapq import heappush, heappop

input = sys.stdin.readline

T, N = map(int, input().split())

process_list = []

for _ in range(N):
    A, B, C = map(int, input().split())

    heappush(process_list, (-C, A, B))

second = 1

while second <= T:
    C, A, B = heappop(process_list)

    B -= 1
    C += 1

    if second <= T:
        print(A)

    if B != 0:
        heappush(process_list, (C, A, B))

    second += 1