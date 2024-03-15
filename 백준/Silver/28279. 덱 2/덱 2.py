import sys
from collections import deque

N = int(input())

int_deque = deque()

for _ in range(N):
    command = tuple(map(int, sys.stdin.readline().split()))

    if command[0] == 1:
        int_deque.appendleft(command[1])
    elif command[0] == 2:
        int_deque.append(command[1])
    elif command[0] == 3 and len(int_deque) == 0:
        print(-1)
    elif command[0] == 3:
        print(int_deque[0])
        int_deque.popleft()
    elif command[0] == 4 and len(int_deque) == 0:
        print(-1)
    elif command[0] == 4:
        print(int_deque[-1])
        int_deque.pop()
    elif command[0] == 5:
        print(len(int_deque))
    elif command[0] == 6 and len(int_deque) == 0:
        print(1)
    elif command[0] == 6:
        print(0)
    elif command[0] == 7 and len(int_deque) == 0:
        print(-1)
    elif command[0] == 7:
        print(int_deque[0])
    elif command[0] == 8 and len(int_deque) == 0:
        print(-1)
    elif command[0] == 8:
        print(int_deque[-1])