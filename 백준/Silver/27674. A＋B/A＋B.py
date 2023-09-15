import sys

for _ in range(int(input())):
    space = sys.stdin.readline()
    s = sorted(list(sys.stdin.readline().rstrip()), reverse=True)

    print(int(''.join(s[:-1])) + int(s[-1]))