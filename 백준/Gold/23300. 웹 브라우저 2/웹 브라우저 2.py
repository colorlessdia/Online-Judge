import sys
from collections import deque

input = sys.stdin.readline

N, Q = map(int, input().split())

backward = deque()
access = deque()
frontward = deque()

for _ in range(Q):
    line = input().rstrip().split()
    command = line[0]

    if command == 'B':
        
        if len(backward) == 0:
            continue
        
        frontward.append(access.pop())
        access.append(backward.pop())
        continue
    
    if command == 'F':
        
        if len(frontward) == 0:
            continue
        
        backward.append(access.pop())
        access.append(frontward.pop())
        continue
    
    if command == 'A':
        page = int(line[1])

        frontward.clear()

        if len(access) != 0:
            backward.append(access.pop())
        
        access.append(page)
        continue
    
    compress = deque()

    for page in backward:
        
        if len(compress) == 0:
            compress.append(page)
            continue
        
        if compress[-1] == page:
            continue
        
        compress.append(page)
    
    backward = compress

print(*access)
print(*reversed(backward)) if 0 < len(backward) else print(-1)
print(*reversed(frontward)) if 0 < len(frontward) else print(-1)