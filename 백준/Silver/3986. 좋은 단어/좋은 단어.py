import sys
from collections import deque

N = int(sys.stdin.readline())

count = 0

for _ in range(N):
    word = sys.stdin.readline().rstrip()

    stack = deque()

    for char in word:
        stack.append(char)

        if len(stack) < 2:
            continue
        
        if stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()

    if len(stack) == 0:
        count += 1

print(count)