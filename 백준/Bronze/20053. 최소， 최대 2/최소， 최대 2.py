import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    number_list = sorted(map(int, sys.stdin.readline().split()))

    print(number_list[0], number_list[-1])