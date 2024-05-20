import sys

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    d = sys.stdin.readline().split()

    count = 0

    for i in range(0, len(d) - 3):
        if int(''.join(d[i:i + 4])) == 2020:
            count += 1
    
    print(count)