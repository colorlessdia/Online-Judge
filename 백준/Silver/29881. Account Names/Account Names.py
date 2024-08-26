import sys

N = int(sys.stdin.readline())

name_dict = dict()

for _ in range(N):
    first_name, last_name = sys.stdin.readline().rstrip().split()

    name_dict[first_name] = last_name

for _ in range(N):
    first_name, account = sys.stdin.readline().rstrip().split()

    print(name_dict[first_name], account)