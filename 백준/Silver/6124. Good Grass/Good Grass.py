import sys

R, C = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

best_square_sum_value = 0
best_square_coordinate = []

for row in range(R - 2):

    for col in range(C - 2):
        square_sum_value = 0
        square_coordinate_x = 0
        square_coordinate_y = 0
        
        for square_row in range(row, row + 3):
            
            for square_col in range(col, col + 3):
                square_sum_value += matrix[square_row][square_col]
            
        square_coordinate_x = str(row + 1)
        square_coordinate_y = str(col + 1)

        if best_square_sum_value < square_sum_value:
            best_square_sum_value = square_sum_value
            best_square_coordinate = [square_coordinate_x, square_coordinate_y]

print(best_square_sum_value)
print(' '.join(best_square_coordinate))