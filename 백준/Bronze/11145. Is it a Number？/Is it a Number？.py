import sys

for _ in range(int(input())):
    s = sys.stdin.readline().strip()
    
    if s.isdigit():
        print(int(s))
    else:
        print('invalid input')