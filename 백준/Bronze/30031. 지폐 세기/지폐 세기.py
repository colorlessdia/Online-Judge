import sys

total = 0

for i in range(int(input())):
    r, c = map(int, sys.stdin.readline().split())

    if r == 136:
        total += 1000
    elif r == 142:
        total += 5000
    elif r == 148:
        total += 10000
    elif r == 154:
        total += 50000
    
print(total)