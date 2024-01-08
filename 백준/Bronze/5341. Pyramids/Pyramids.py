import sys
while 1:
    n = int(sys.stdin.readline())
    if n == 0: break
    cnt = 0
    for i in range(1, n + 1):
        cnt += i
    print(cnt)