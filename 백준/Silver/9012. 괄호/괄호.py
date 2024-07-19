import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    line = sys.stdin.readline().rstrip()

    parenthesis_stack = deque()

    for parenthesis in line:
        parenthesis_stack.append(parenthesis)

        if parenthesis == '(':
            continue
        
        is_vaild = False
        count = 0

        for i in range(2, len(parenthesis_stack) + 1):
            if parenthesis_stack[-i] == '(':
                is_vaild = True
                count = i
                break
        
        if not is_vaild:
            break

        for _ in range(count):
            parenthesis_stack.pop()
    
    if len(parenthesis_stack) == 0:
        print('YES')
    else:
        print('NO')