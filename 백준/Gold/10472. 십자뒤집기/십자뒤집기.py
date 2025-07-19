import sys
from collections import deque

def BFS(target):
    queue = deque([(0, 0)])
    visited = [False] * (1 << 9)
    visited[0] = 1

    d = [
            (0, 1, 3), (0, 1, 2, 4), (1, 2, 5),
            (0, 3, 4, 6), (1, 3, 4, 5, 7), (2, 4, 5, 8), 
            (3, 6, 7), (4, 6, 7, 8), (5, 7, 8)
        ]

    while queue:
        bit, count = queue.popleft()

        if bit == target:
            return count
        
        for i in range(9):
            positions = d[i]
            temp = bit

            for position in positions:
                temp ^= (1 << position)
            
            if visited[temp]:
                continue

            queue.append((temp, count + 1))
            visited[temp] = True
    
    return 0

input = sys.stdin.readline

P = int(input())

for _ in range(P):
    target = 0
    position = 0

    for _ in range(3):
        row = input().rstrip()

        for col in row:
            
            if col == '*':
                target |= (1 << position)
            
            position += 1
        
    print(BFS(target))