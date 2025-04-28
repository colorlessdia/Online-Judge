from collections import deque

N = int(input())
A_stack = deque(map(int, input().split()))

chain_list = [0] * N
stack = deque()
stack.append(A_stack.pop())

for i in range(N - 2, -1, -1):
    A = A_stack.pop()
    
    if A < stack[-1]:
        chain_list[i] = len(stack)
        stack.append(A)
        continue

    while 0 < len(stack):
        stack.pop()

        if len(stack) == 0:
            stack.append(A)
            break

        if A < stack[-1]:
            chain_list[i] = len(stack)
            stack.append(A)
            break

print(*chain_list)