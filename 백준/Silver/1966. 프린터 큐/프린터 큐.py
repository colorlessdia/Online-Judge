import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    i_sequence = map(int, input().split())

    i_queue = deque()
    i_count = dict()

    for index, i in enumerate(i_sequence):
        i_queue.append((index, i))
        i_count[i] = i_count.get(i, 0) + 1

    count = 0

    while i_queue:
        index, i = i_queue.popleft()
        is_find = False

        for j in range(i + 1, 9 + 1):
            
            if i_count.get(j, 0):
                is_find = True
                break

        if is_find:
            i_queue.append((index, i))
            continue
        
        i_count[i] -= 1
        count += 1
        
        if index == M:
            print(count)
            break