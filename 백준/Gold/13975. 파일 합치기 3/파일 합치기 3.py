import sys
import heapq as hq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    size_list = list(map(int, input().split()))

    hq.heapify(size_list)

    cost = 0

    while 1 < len(size_list):
        size_1 = hq.heappop(size_list)
        size_2 = hq.heappop(size_list)

        merge_size = size_1 + size_2

        cost += merge_size

        hq.heappush(size_list, merge_size)
    
    print(cost)