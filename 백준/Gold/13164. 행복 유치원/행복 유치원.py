from heapq import heappush, heappop

N, K = map(int, input().split())
height_list = list(map(int, input().split()))

total_cost = 0
cost_max_heap = []

for i in range(N - 1):
    difference = height_list[i + 1] - height_list[i]

    total_cost += difference

    heappush(cost_max_heap, -difference)

for j in range(K - 1):
    max_cost = -heappop(cost_max_heap)

    total_cost -= max_cost

print(total_cost)