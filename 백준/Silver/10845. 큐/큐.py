import sys
from collections import deque

N = int(input())

int_queue = deque()

for _ in range(N):
    command = sys.stdin.readline().rstrip().split()

    if command[0] == 'push':
        int_queue.append(int(command[1]))
    elif command[0] == 'pop' and len(int_queue) == 0:
        print(-1)
    elif command[0] == 'pop':
        print(int_queue[0])
        int_queue.popleft()
    elif command[0] == 'size':
        print(len(int_queue))
    elif command[0] == 'empty' and len(int_queue) == 0:
        print(1)
    elif command[0] == 'empty':
        print(0)
    elif command[0] == 'front' and len(int_queue) == 0:
        print(-1)
    elif command[0] == 'front':
        print(int_queue[0])
    elif command[0] == 'back' and len(int_queue) == 0:
        print(-1)
    elif command[0] == 'back':
        print(int_queue[-1])