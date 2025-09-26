import sys
from heapq import heapify, heappush, heappop

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    size_list = list(map(int, input().split()))

    heapify(size_list)

    total_size = 0
    current_size = []

    while size_list:
        
        if len(current_size) < 2:
            current_size.append(heappop(size_list))
            continue

        size_sum = sum(current_size)
        total_size += size_sum

        heappush(size_list, size_sum)

        current_size.clear()
        current_size.append(heappop(size_list))

    total_size += sum(current_size)

    print(total_size)