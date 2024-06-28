import sys

s = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())

start_index = 0
end_index = 0

for i in range(1, n + 1):
    start, length = map(int, sys.stdin.readline().split())

    start_index += start

    if i == n:
        end_index = start_index + length

print(s[start_index:end_index])