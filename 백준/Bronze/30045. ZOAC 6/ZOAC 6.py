import sys

cnt = 0

for _ in range(int(input())):
    s = sys.stdin.readline().rstrip()

    if ('01' in s) or ('OI' in s):
        cnt += 1
    
print(cnt)