board = input()

is_possible = True

completed_board = ''

x_count = 0

for i, char in enumerate(board, 1):

    if char == 'X':
        x_count += 1

    if (
        (0 < x_count and char == '.') or
        (0 < x_count and i == len(board))
      ):
        
        if x_count % 2 != 0:
            is_possible = False
            break
        
        a_count = x_count // 4
        b_count = x_count % 4 // 2

        completed_board += ('AAAA' * a_count) + ('BB' * b_count)

        x_count = 0
    
    if char == '.':
        completed_board += '.'

if is_possible:
    print(completed_board)
else:
    print(-1)