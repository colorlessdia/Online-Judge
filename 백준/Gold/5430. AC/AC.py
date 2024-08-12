import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    x = deque(sys.stdin.readline().rstrip()[1:-1].split(','))

    is_reverse = False
    is_empty = False
    length = n

    for function in p:
        
        if function == 'R':
            is_reverse = not is_reverse
            continue
        
        if length <= 0:
            is_empty = True
            break
        
        if is_reverse:
            x.pop()
        else:
            x.popleft()
        
        length -= 1
    
    if is_empty:
        print('error')
        continue
    
    if is_reverse:
        print(f'[{",".join(reversed(x))}]')
    else:
        print(f'[{",".join(x)}]')