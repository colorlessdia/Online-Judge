import sys

N, M = map(int, sys.stdin.readline().split())

history = [sys.stdin.readline().rstrip().split() for _ in range(M)]

sorted_history = sorted(history, key=lambda x: (int(x[1]), int(x[0])))

result = ''

for keyboard, second, key in sorted_history:
    result += key

print(result)