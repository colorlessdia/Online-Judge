import sys
from collections import deque

input = sys.stdin.readline

Q = int(input())

stack = deque()
persistent_stack = deque()

for _ in range(Q):
    query = list(map(int, input().split()))
    query_type = query[0]

    if query_type == 1:
        i = query[1]

        stack.append(i)
        persistent_stack.append((i, 0))
    elif query_type == 2:
        i = stack.pop()
        persistent_stack.append((i, 1))
    elif query_type == 3:
        j = query[1]

        for _ in range(j):
            v, t = persistent_stack.pop()

            if t:
                stack.append(v)
            else:
                stack.pop()

    elif query_type == 4:
        print(len(stack))
    elif query_type == 5:

        if not stack:
            print(-1)
        else:
            print(stack[-1])