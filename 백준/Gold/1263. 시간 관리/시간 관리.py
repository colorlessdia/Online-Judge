import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())

schedule_list = []

for _ in range(N):
    T, S = map(int, input().split())

    heappush(schedule_list, (-S, -T))

time = 1000000

while schedule_list:
    S, T = map(lambda x: -x, heappop(schedule_list))

    if S <= time:
        time = S - T
    else:
        time -= T

if 0 <= time:
    print(time)
else:
    print(-1)