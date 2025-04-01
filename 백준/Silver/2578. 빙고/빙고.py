def check_bingo(bingo):
    bingo_count = 0
    
    for row in bingo:
        check_row = all([1 if col == 0 else 0 for col in row])

        if check_row:
            bingo_count += 1
    
    cols = [[bingo[row][col] for row in range(5)] for col in range(5)]
    
    for col in cols:
        check_col = all([1 if row == 0 else 0 for row in col])

        if check_col:
            bingo_count += 1
    
    diagonal_to_left = []
    diagonal_to_right = []

    for i in range(5):
        diagonal_to_left.append(bingo[i][i])
        diagonal_to_right.append(bingo[i][4 - i])
    
    if sum(diagonal_to_left) == 0:
        bingo_count += 1

    if sum(diagonal_to_right) == 0:
        bingo_count += 1

    if bingo_count < 3:
        return False
    
    return True

bingo = [[0 for _ in range(5)] for _ in range(5)]
bingo_coordinates = dict()

for i in range(5):
    bingo_numbers = list(map(int, input().split()))

    for j in range(5):
        bingo_number = bingo_numbers[j]

        bingo[i][j] = bingo_number
        bingo_coordinates[bingo_number] = (i, j)

call_count = 1
is_completed = False

for _ in range(5):
    call_sequence = map(int, input().split())

    if is_completed:
        continue

    for call_number in call_sequence:
        p, q = bingo_coordinates[call_number]

        bingo[p][q] = 0
        
        if check_bingo(bingo):
            is_completed = True
            break
        
        call_count += 1

print(call_count)