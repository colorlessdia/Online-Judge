import sys

def matched_coordinate(string, x, y):
    x, y = x, y

    if string == 'L':
        x -= 1
    
    if string == 'R':
        x += 1

    if string == 'B':
        y -= 1

    if string == 'T':
        y += 1

    if string == 'LB':
        x -= 1
        y -= 1
    
    if string == 'RB':
        x += 1
        y -= 1

    if string == 'LT':
        x -= 1
        y += 1

    if string == 'RT':
        x += 1
        y += 1
    
    return (x, y)

def is_valid_coordinate(x, y):
    
    if 1 <= x <= 8 and 1 <= y <= 8:
        return True
    
    return False

chess_board = dict()

for row in range(1, 8 + 1):
    board_alphabat = chr(row + ord('A') - 1)
    
    for col in range(1, 8 + 1):
        board_number = str(col)
        coordinate = board_alphabat + board_number

        chess_board[coordinate] = (row, col)
        chess_board[(row, col)] = coordinate

K, S, N = sys.stdin.readline().rstrip().split()

kx, ky = chess_board[K]
sx, sy = chess_board[S]

for _ in range(int(N)):
    string = sys.stdin.readline().rstrip()

    tkx, tky = matched_coordinate(string, kx, ky)
    
    if not is_valid_coordinate(tkx, tky):
        continue
    
    if not (tkx == sx and tky == sy):
        kx, ky = tkx, tky
        continue
    
    tsx, tsy = matched_coordinate(string, sx, sy)

    if not is_valid_coordinate(tsx, tsy):
        continue
    
    kx, ky = tkx, tky
    sx, sy = tsx, tsy

print(chess_board[(kx, ky)])
print(chess_board[(sx, sy)])