from collections import deque

P, S = input().split()

p = deque(P)
is_valid = True

for c in S:
    
    if len(p) == 0:
        break

    if c != p[0] and c in p:
        is_valid = False
        break

    if c == p[0]:
        p.popleft()

if len(p) != 0:
    is_valid = False

if is_valid:
    print('PASS')
else:
    print('FAIL')