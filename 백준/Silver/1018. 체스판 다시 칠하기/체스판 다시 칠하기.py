import sys

input = sys.stdin.readline

N, M = map(int, input().split())
W = 'WB' * 4
B = 'BW' * 4

white_board = [W if w % 2 == 0 else B for w in range(8)]
black_board = [B if b % 2 == 0 else W for b in range(8)]
board = [list(input().rstrip()) for _ in range(N)]

start_coordinates = []

for i in range(N - 7):
    
    for j in range(M - 7):
        start_coordinates.append((i, j))

minimum_difference = 64

for i, j in start_coordinates:
    white_difference = 0
    black_difference = 0
    
    for r in range(i, i + 8):
        
        for c in range(j, j + 8):
            cell = board[r][c]
            white = white_board[r - i][c - j]
            black = black_board[r - i][c - j]

            if cell != white:
                white_difference += 1

            if cell != black:
                black_difference += 1
        
    if white_difference < minimum_difference:
        minimum_difference = white_difference
    
    if black_difference < minimum_difference:
        minimum_difference = black_difference

print(minimum_difference)