import sys

input = sys.stdin.readline

eight_number_list = [int('8' * i) for i in range(1, 18 + 1)]

T = int(input())

for _ in range(T):
    N = input().rstrip()

    index = len(N)
    N = int(N)

    target = eight_number_list[index]
    count = 0

    while 0 < N:
        
        if N < target:
            index -= 1

            if index < 0:
                break

            target = eight_number_list[index]
            continue

        N -= target
        count += 1

    if N == 0 and count <= 8:
        print('Yes')
    else:
        print('No')