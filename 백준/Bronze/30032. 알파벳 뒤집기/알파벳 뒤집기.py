import sys

n, d = map(int, input().split())

for _ in range(n):
    s = sys.stdin.readline().rstrip()

    new_line = ''

    for ss in s:
        if d == 1:
            if ss == 'd':
                new_line += 'q'
            elif ss == 'b':
                new_line += 'p'
            elif ss == 'q':
                new_line += 'd'
            elif ss == 'p':
                new_line += 'b'
        else:
            if ss == 'd':
                new_line += 'b'
            elif ss == 'b':
                new_line += 'd'
            elif ss == 'q':
                new_line += 'p'
            elif ss == 'p':
                new_line += 'q'
    
    print(new_line)