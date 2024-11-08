import sys

N, C = map(int, sys.stdin.readline().split())
time_line = [0] * (C + 1)

is_full = False

for _ in range(N):
    time = int(sys.stdin.readline())

    if is_full:
        continue

    if time == 1:
        is_full = True

    for i in range(time, C + 1, time):
        time_line[i] = 1

if is_full:
    print(C)
else:
    print(sum(time_line))