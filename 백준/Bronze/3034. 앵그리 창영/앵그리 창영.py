import sys
import math
n, w, h = map(int, input().split())

for _ in range(n):
    num = int(sys.stdin.readline())

    if num <= w or num <= h or num <= math.sqrt(w ** 2 + h ** 2):
        print('DA')
    else:
        print('NE')