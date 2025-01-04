import sys

N, M = map(int, sys.stdin.readline().split())

order_list = []

for _ in range(N):
    line = sys.stdin.readline().rstrip().split()

    if len(line) == 3:
        n, t = map(int, line[1:])
        
        order_list.append([n, t])
    elif len(line) == 2:
        n = int(line[1])
        
        index = [i for i in range(len(order_list)) if order_list[i][0] == n][0]
        
        order_list.pop(index)
    elif len(line) == 1:
        order_list.sort(key=lambda x: (x[1], x[0]))

    if len(order_list) == 0:
        print('sleep')
    else:
        print(*[table for table, _ in order_list])