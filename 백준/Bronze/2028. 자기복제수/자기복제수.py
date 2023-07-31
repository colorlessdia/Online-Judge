import sys

for _ in range(int(input())):
    n = sys.stdin.readline().rstrip()
    length = len(n)
    
    if n == str(int(n) ** 2)[-1 * length:]:
        print('YES')
    else:
        print('NO')