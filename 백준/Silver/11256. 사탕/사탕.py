import sys

T = int(input())

for _ in range(T):
    J, N = map(int, sys.stdin.readline().split())

    box_list = []

    for _ in range(N):
        R, C = map(int, sys.stdin.readline().split())

        box_list.append(R * C)
    
    box_count = 0

    for box in reversed(sorted(box_list)):
        J -= box

        box_count += 1

        if J <= 0:
            break
    
    print(box_count)