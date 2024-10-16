import sys

N = int(sys.stdin.readline())

history_list = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

sorted_history_list = sorted(history_list, key=lambda x: (x[0], x[1], x[2]))

for history in sorted_history_list:
    print(*history)