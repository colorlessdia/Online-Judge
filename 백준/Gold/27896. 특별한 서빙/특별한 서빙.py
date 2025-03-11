from heapq import heappush, heappop

N, M = map(int, input().split())
x_sequence = map(int, input().split())

negative = 0
eggplant = 0
x_list = []

for x in x_sequence:
    negative += x
    heappush(x_list, -x)

    if negative < M:
        continue
    
    negative += heappop(x_list) * 2
    eggplant += 1

print(eggplant)