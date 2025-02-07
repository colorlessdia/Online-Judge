import heapq as hq

N, M = map(int, input().split())
t_list = sorted(map(int, input().split()), key=lambda x: -x)

outlet = [0] * M

for t in t_list:
    accumulated_time = hq.heappop(outlet)

    hq.heappush(outlet, accumulated_time + t)

print(max(outlet))