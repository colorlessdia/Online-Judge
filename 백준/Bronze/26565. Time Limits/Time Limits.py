import sys
from math import ceil

input = sys.stdin.readline

M = int(input())

for _ in range(M):
    N, S = map(int, input().split())
    T_max = max(map(int, input().split()))
    
    L = ceil((T_max * S) / 1000)

    print(L)