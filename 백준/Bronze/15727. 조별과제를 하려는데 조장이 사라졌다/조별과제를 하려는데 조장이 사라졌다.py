import sys

l = int(sys.stdin.readline())
t = 0

if l % 5 == 0:
    t = l // 5
else:
    t = (l // 5) + 1

print(t)