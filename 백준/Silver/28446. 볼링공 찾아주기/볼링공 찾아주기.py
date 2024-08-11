import sys

M = int(sys.stdin.readline())

locker = dict()

for _ in range(M):
    line = list(map(int, sys.stdin.readline().rstrip().split()))

    request = line[0]
    weight = line[-1]

    if request == 1:
        x = line[1]
        locker[weight] = x
        continue
    
    print(locker[weight])