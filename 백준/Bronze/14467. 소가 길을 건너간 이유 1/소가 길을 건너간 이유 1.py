import sys

N = int(sys.stdin.readline())

cow_dict = dict()

count = 0

for _ in range(N):
    cow, direction = map(int, sys.stdin.readline().split())

    if cow in cow_dict:
        if cow_dict[cow][1] != direction:
            cow_dict[cow][0] += 1
            cow_dict[cow][1] = direction

            count += 1
    else:
        cow_dict[cow] = [0, direction]

print(count)