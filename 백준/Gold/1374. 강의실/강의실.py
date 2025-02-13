import sys
from heapq import heappush, heappop

input = sys.stdin.readline

schedule_list = []

N = int(input())

for _ in range(N):
    _, start, end = map(int, input().split())

    heappush(schedule_list, (start, end))

classroom_list = [heappop(schedule_list)[1]]

for _ in range(N - 1):
    start, end = heappop(schedule_list)
    class_end = heappop(classroom_list)
    
    if start < class_end:
        heappush(classroom_list, class_end)

    heappush(classroom_list, end)

classroom_count = len(classroom_list)

print(classroom_count)