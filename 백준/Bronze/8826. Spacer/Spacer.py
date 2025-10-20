import sys

input = sys.stdin.readline

Z = int(input())

for _ in range(Z):
    N = int(input())
    move_list = input().rstrip()

    x, y = 0, 0

    for move in move_list:
        
        if move == 'N':
            y += 1
        elif move == 'S':
            y -= 1
        elif move == 'E':
            x += 1
        elif move == 'W':
            x -= 1
    
    distance = abs(x) + abs(y)

    print(distance)