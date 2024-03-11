import sys
from math import ceil

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    print(ceil(n / 2))