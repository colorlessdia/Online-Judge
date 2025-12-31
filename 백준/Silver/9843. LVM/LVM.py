import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
command_list = [input().rstrip().split() for _ in range(N)]

stack = deque()
register = 0
index = 0

while index < N:
    command = command_list[index]
    C = command[0]

    if C == 'PUSH':
        x = int(command[1])
        stack.append(x)
    elif C == 'STORE':
        register = stack.pop()
    elif C == 'LOAD':
        stack.append(register)
    elif C == 'PLUS':
        x1 = stack.pop()
        x2 = stack.pop()
        stack.append(x1 + x2)
    elif C == 'TIMES':
        x1 = stack.pop()
        x2 = stack.pop()
        stack.append(x1 * x2)
    elif C == 'IFZERO':
        x = stack.pop()
        n = int(command[1])

        if x == 0:
            index = n
            continue

    elif C == 'DONE':
        print(stack[-1])
        break

    index += 1