import sys

N = int(sys.stdin.readline())

for _ in range(N):
    angles = list(map(int, sys.stdin.readline().split()))
    angle_sum = sum(angles)

    message = 'Check'

    if angle_sum == 180:
        message = 'Seems OK'
    
    print(f'{angles[0]} {angles[1]} {angles[2]} {message}')