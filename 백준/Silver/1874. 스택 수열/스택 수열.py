import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

number_sequence = [int(input()) for _ in range(N)]
operator_stack = deque()
stack = deque()

index = 0

for i in range(1, N + 1):
    stack.append(i)
    operator_stack.append('+')

    while stack:
        
        if stack[-1] != number_sequence[index]:
            break
        
        stack.pop()
        operator_stack.append('-')

        index += 1

if not stack:
    
    for operator in operator_stack:
        print(operator)
else:
    print('NO')