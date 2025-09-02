import sys

input = sys.stdin.readline

sequence = [1] * (100 + 1)

for i in range(4, 100 + 1):
    sequence[i] = sequence[i - 2] + sequence[i - 3]

T = int(input())

for _ in range(T):
    N = int(input())

    print(sequence[N])