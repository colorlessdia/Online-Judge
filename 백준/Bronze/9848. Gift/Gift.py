import sys

n, k = map(int, sys.stdin.readline().split())
before = 0
diff = 0
cnt = 0

for _ in range(n):
    s = int(sys.stdin.readline())
    
    if before == 0:
        before = s
    else:
        diff = before - s
        before = s
    
    if k <= diff:
        cnt += 1

print(cnt)