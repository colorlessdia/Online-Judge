import sys

input = sys.stdin.readline

while True:
    line = list(map(int, input().split()))
    K = line[0]

    if K == 0:
        break

    P_sequence = line[1:]
    number_list = []

    for i, P in enumerate(P_sequence, 1):
        j = P - len(number_list)
        li = [i] * j

        number_list.extend(li)
    
    print(*number_list)