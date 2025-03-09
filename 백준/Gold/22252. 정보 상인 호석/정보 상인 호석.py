import sys
from heapq import heappush, heappop

input = sys.stdin.readline

gorilla_dict = dict()
cost = 0

Q = int(input())

for _ in range(Q):
    line = input().rstrip().split()

    query = line[0]
    gorilla = line[1]
    count = int(line[2])

    if query == '1':
        info_sequence = map(int, line[3:])
        
        if gorilla not in gorilla_dict:
            gorilla_dict[gorilla] = []
        
        for info in info_sequence:
            heappush(gorilla_dict[gorilla], -info)

    elif query == '2':

        if gorilla not in gorilla_dict:
            continue
        
        length = len(gorilla_dict[gorilla])
        
        if length < count:
            count = length

        for _ in range(count):
            info = -heappop(gorilla_dict[gorilla])
            cost += info

print(cost)