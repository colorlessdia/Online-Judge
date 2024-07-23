import sys
from collections import deque

matched_bracket = dict(zip(list(')}]'), list('({[')))

while True:
    line = sys.stdin.readline().rstrip()

    if line == '#':
        break
    
    stack = deque([])

    for char in line:
        
        if char not in '({[]})':
            continue
        
        if char in '({[':
            stack.append(char)
            continue
        
        if char in ']})':
            stack.append(char)
    
        if matched_bracket[char] == stack[-2]:
            stack.pop()
            stack.pop()
            
    if len(stack) == 0:
        print('Legal')
    else:
        print('Illegal')