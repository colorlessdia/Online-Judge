import sys

while 1:
    a, b, c = map(int, sys.stdin.readline().split())
    
    if a == 0 and b == 0 and c == 0: break
    
    if (c - a) % b == 0 and (c - a) // b + 1 > 0:
        print((c - a) // b + 1)
    else:
        print('X')