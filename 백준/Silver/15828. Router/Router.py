import sys

buffer_size = int(input())
buffer = []

while 1:
    p = int(sys.stdin.readline().rstrip())
    
    if p < 0: break
    
    if 0 < p and len(buffer) < buffer_size:
        buffer.append(p)
    elif p == 0:
        buffer.pop(0)

if len(buffer) == 0:
    print('empty')
else:
    print(' '.join(map(str, buffer)))