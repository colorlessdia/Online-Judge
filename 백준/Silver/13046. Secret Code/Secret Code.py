import sys

s = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())

char_dict = dict(zip(list(s), [1] * len(s)))

for _ in range(n):
    line = sys.stdin.readline().rstrip()

    a, b = 0, 0

    for c1, c2 in zip(line, s):
        
        if c1 not in char_dict:
            continue
        
        if c1 == c2:
            a += 1
            continue
        
        b += 1

    print(a, b)