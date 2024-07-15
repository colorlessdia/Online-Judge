import sys

N, I = map(int, sys.stdin.readline().split())

handle_list = sorted([sys.stdin.readline().rstrip() for _ in range(N)])

print(handle_list[I - 1])