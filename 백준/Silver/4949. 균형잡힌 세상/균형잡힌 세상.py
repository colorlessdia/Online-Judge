import sys
from collections import deque

input = sys.stdin.readline

while 1:
    line = input().rstrip()

    if line == '.':
        break
    
    is_balanced = True
    stack = deque()

    for char in line:
        
        if not is_balanced:
            break
        
        if char not in ['[', ']', '(', ')']:
            continue
        
        if char in ['[', '(']:
            stack.append(char)
            continue
        
        if not stack:
            is_balanced = False
            break
        
        pop_item = stack.pop()

        if char == ']':
            
            if pop_item != '[':
                is_balanced = False
                break
            
            continue
        
        if char == ')':
            
            if pop_item != '(':
                is_balanced = False
                break
            
            continue

    if is_balanced and (not stack):
        print('yes')
    else:
        print('no')