import sys
t = int(sys.stdin.readline())

for i in range(t):
    s = sys.stdin.readline().rstrip()
    print(s[0] + s[len(s) - 1])