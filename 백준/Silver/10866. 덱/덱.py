import sys
from collections import deque

N = int(input())

int_deque = deque()

for _ in range(N):
    command = sys.stdin.readline().rstrip().split()

    if command[0] == 'push_front':
        int_deque.appendleft(command[1])
    elif command[0] == 'push_back':
        int_deque.append(command[1])
    elif command[0] == 'pop_front' and len(int_deque) == 0:
        print(-1)
    elif command[0] == 'pop_front':
        print(int_deque[0])
        int_deque.popleft()
    elif command[0] == 'pop_back' and len(int_deque) == 0:
        print(-1)
    elif command[0] == 'pop_back':
        print(int_deque[-1])
        int_deque.pop()
    elif command[0] == 'size':
        print(len(int_deque))
    elif command[0] == 'empty' and len(int_deque) == 0:
        print(1)
    elif command[0] == 'empty':
        print(0)
    elif command[0] == 'front' and len(int_deque) == 0:
        print(-1)
    elif command[0] == 'front':
        print(int_deque[0])
    elif command[0] == 'back' and len(int_deque) == 0:
        print(-1)
    elif command[0] == 'back':
        print(int_deque[-1])