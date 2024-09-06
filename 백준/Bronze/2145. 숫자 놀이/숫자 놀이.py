import sys

while True:
    N = sys.stdin.readline().rstrip()

    if N == '0':
        break
    
    if len(N) == 1:
        print(N)
        continue
    
    while 1 < len(N):
        N = str(sum(map(int, list(N))))

    print(N)