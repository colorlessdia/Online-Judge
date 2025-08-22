import sys

def calc_coordinate(x, y, path):

    if path == 'N':
        return (x, y + 1)
    
    if path == 'S':
        return (x, y - 1)
    
    if path == 'E':
        return (x + 1, y)
    
    if path == 'W':
        return (x - 1, y)

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    path_sequence = input().rstrip()
    length = len(path_sequence)

    coordinates = [0] * length
    x, y = 0, 0

    for i in range(length):
        path = path_sequence[i]
        p, q = calc_coordinate(x, y, path)

        coordinates[i] = (p,  q)
        x, y = p, q

    sum1 = 0
    sum2 = 0

    for i in range(length):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[(i + 1) % length]

        sum1 += x1 * y2
        sum2 += y1 * x2

    sign = 'CW' if (sum1 - sum2) < 0 else 'CCW'

    print(sign)