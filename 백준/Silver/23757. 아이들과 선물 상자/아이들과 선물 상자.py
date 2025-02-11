from heapq import heappush, heappop

N, M = map(int, input().split())
c_list = list(map(int, input().split()))
w_list = list(map(int, input().split()))

count_list = []

for count in c_list:
    heappush(count_list, -count)

is_valid = True

for wish in w_list:
    count = -heappop(count_list)
    difference = count - wish

    if difference < 0:
        is_valid = False
        break
    
    heappush(count_list, -difference)

if is_valid:
    print(1)
else:
    print(0)