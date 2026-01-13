import sys

input = sys.stdin.readline

line = list(map(int, input().split()))
N = line[0]
A_set = set(line[1:])
M = int(input())

count = 0

for _ in range(M):
    li = list(map(int, input().split()))
    K = li[0]
    B_list = li[1:]

    is_valid = True

    for B in B_list:

        if B in A_set:
            is_valid = False
            break

    if is_valid:
        count += 1

print(count)