import sys
from collections import deque
from heapq import heappush, heappop

input = sys.stdin.readline

N, M, K = map(int, input().split())

lines = deque([deque() for _ in range(M)])

for i in range(N):
    D, H = map(int, input().split())
    L = i % M
    is_deka = 1 if i == K else 0

    lines[L].append((-D, -H, L, is_deka))

leading_group = []

for i in range(M):

    if lines[i]:
        heappush(leading_group, lines[i].popleft())

waiting_count = 0

while leading_group:
    D, H, L, is_deka = heappop(leading_group)

    if is_deka:
        break

    if lines[L]:
        heappush(leading_group, lines[L].popleft())

    waiting_count += 1

print(waiting_count)