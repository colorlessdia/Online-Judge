import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

count = 0

for i in nums:
    if (i == v):
        count += 1

print(count)