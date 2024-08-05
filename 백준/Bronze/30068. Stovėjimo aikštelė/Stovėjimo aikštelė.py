import sys

M = int(sys.stdin.readline())

parking_history = dict()

for _ in range(M):
    T, N = map(int, sys.stdin.readline().split())

    if N in parking_history:
        print(N, T - parking_history[N])
    else:
        parking_history[N] = T