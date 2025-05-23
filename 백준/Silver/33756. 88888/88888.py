import sys

input = sys.stdin.readline

eight_number_list = [int('8' * i) for i in range(18, 0, -1)]

T = int(input())

for _ in range(T):
    N = int(input())

    count = 0

    for eight_number in eight_number_list:
        
        if N < eight_number:
            continue
        
        while eight_number <= N:
            N -= eight_number
            count += 1

    result = 'Yes' if N == 0 and count <= 8 else 'No'

    print(result)