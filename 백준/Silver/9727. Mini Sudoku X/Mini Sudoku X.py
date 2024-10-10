import sys

T = int(sys.stdin.readline())

for t in range(1, T + 1):
    is_valid = True

    A = [0] * 6
    B = [[] for _ in range(6)]
    
    for i in range(6):
        A[i] = list(map(int, sys.stdin.readline().split()))
    
        for j, k in enumerate(A[i]):
            B[j].append(k)
    
    for l in range(6):
        A_row_length = len(set(A[l]))
        B_row_length = len(set(B[l]))

        if any([A_row_length != 6, B_row_length != 6]):
            is_valid = False
            break
    
    if is_valid:
        C = []
        D = []

        for m in range(6):
            
            for n in range(6):
                
                if m == n:
                    C.append(A[m][n])
                    continue
                
                if m + n == 5:
                    D.append(A[m][n])
                    continue
        
        is_valid = all([len(set(C)) == 6, len(set(D)) == 6])

    sudoku_X_state = 1 if is_valid else 0

    print(f'Case#{t}: {sudoku_X_state}')