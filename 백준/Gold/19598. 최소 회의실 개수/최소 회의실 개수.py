import sys
from heapq import heappush, heappop

input = sys.stdin.readline

schedule_list = []

N = int(input())

for _ in range(N):
    start, end = map(int, input().split())

    heappush(schedule_list, (start, end))

cabinet_schedule = []

for _ in range(N):
    start, end = heappop(schedule_list)

    if len(cabinet_schedule) == 0:
        heappush(cabinet_schedule, end)
        continue
    
    cabinet_end = heappop(cabinet_schedule)

    if start < cabinet_end:
        heappush(cabinet_schedule, cabinet_end)

    heappush(cabinet_schedule, end)

count = len(cabinet_schedule)

print(count)