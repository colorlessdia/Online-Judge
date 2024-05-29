import sys

T = int(sys.stdin.readline())

for i in range(1, T + 1):
    N = int(sys.stdin.readline())

    fabric_list = [sys.stdin.readline().rstrip().split() for _ in range(N)]

    ada_list = sorted(fabric_list, key=lambda x: (x[0], int(x[2])))
    charles_list = sorted(fabric_list, key=lambda x: (int(x[1]), int(x[2])))

    count = 0

    for ada, charles in zip(ada_list, charles_list):
        if ada[-1] == charles[-1]:
            count += 1
    
    print(f'Case #{i}: {count}')