import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())

ascending_list = []
descending_list = []
problem_state = {}

for _ in range(N):
    P, L = map(int, input().split())

    heappush(ascending_list, (L, P))
    heappush(descending_list, (-L, -P))

    problem_state[P] = L

M = int(input())

for _ in range(M):
    line = input().rstrip().split()
    command = line[0]

    if command == 'add':
        number, level = map(int, line[1:])

        heappush(ascending_list, (level, number))
        heappush(descending_list, (-level, -number))
        
        problem_state[number] = level
        continue
    
    if command == 'solved':
        number = int(line[1])

        del problem_state[number]
        continue
    
    X = int(line[1])

    if X < 0:

        while ascending_list:
            l, p = heappop(ascending_list)

            if p not in problem_state:
                continue
            
            if l != problem_state[p]:
                continue
            
            print(p)
            heappush(ascending_list, (l, p))
            break
    else:

        while descending_list:
            l, p = heappop(descending_list)
            l, p = -l, -p

            if p not in problem_state:
                continue
            
            if l != problem_state[p]:
                continue
            
            print(p)
            heappush(descending_list, (-l, -p))
            break