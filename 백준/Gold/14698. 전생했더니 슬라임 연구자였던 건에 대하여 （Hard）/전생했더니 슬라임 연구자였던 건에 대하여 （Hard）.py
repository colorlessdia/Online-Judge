import sys
from heapq import heapify, heappush, heappop

input = sys.stdin.readline

T = int(input())

D = 1000000007

for _ in range(T):
    N = int(input())
    slime_list = list(map(int, input().split()))

    if N == 1:
        print(1)
        continue
    
    heapify(slime_list)

    energy = 1

    while 1 < len(slime_list):
        A = heappop(slime_list)
        B = heappop(slime_list)

        C = A * B

        energy *= C

        heappush(slime_list, C)
    
    print(energy % D)