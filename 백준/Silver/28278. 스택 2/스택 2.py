import sys

stack = []

for _ in range(int(input())):
    s = list(map(int, sys.stdin.readline().split()))
    order = s[0]

    if order == 1:
        stack.append(s[1])
    elif order == 2 and len(stack) != 0:
        print(stack[-1])
        stack.pop(-1)
    elif order == 2 and len(stack) == 0:
        print(-1)
    elif order == 3:
        print(len(stack))
    elif order == 4 and len(stack) == 0:
        print(1)
    elif order == 4 and len(stack) != 0:
        print(0)
    elif order == 5 and len(stack) != 0:
        print(stack[-1])
    elif order == 5 and len(stack) == 0:
        print(-1)