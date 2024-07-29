def calc_coordinate(number):
    row = 0
    col = 0

    if number % 4 == 0:
        row = 4
        col = number // 4
    else:
        row = number % 4
        col = (number // 4) + 1

    return (row, col)

a, b = map(int, input().split())

a_row, a_col = calc_coordinate(a)
b_row, b_col = calc_coordinate(b)

print(abs(b_col - a_col) + abs(b_row - a_row))