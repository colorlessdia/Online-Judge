from collections import deque

S = input()

stack = deque()

for s in S:
    stack.append(s)

    if s != ')':
        continue
    
    if len(stack) < 2:
        continue
    
    if stack[-2] == '(':
        stack.pop()
        stack.pop()

print(len(stack))