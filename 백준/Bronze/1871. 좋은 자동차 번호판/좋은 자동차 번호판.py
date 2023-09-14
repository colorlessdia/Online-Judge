import sys

for _ in range(int(input())):
    f, b = sys.stdin.readline().rstrip().split('-')
    
    base = ord('A')
    
    sum_front = 0
    
    for i, ff in enumerate(f[::-1]):
        sum_front += (ord(ff) - base) * (26 ** i)
    
    result = (sum_front - int(b))
    
    if result < 0:
        result *= -1
    
    print('nice') if result <= 100 else print('not nice')