import sys

R, C = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
median_matrix = []

T = int(sys.stdin.readline())

filter_count = 0

for r in range(R - 2):
    median_list = []
    
    for c in range(C - 2):
        filter_matrix = []
        
        for i in range(3):
            
            for j in range(3):
                filter_matrix.append(matrix[r + i][c + j])
    
        filter_matrix.sort()

        median = filter_matrix[4]

        if T <= median:
            filter_count += 1

        median_list.append(median)

    median_matrix.append(median_list)

print(filter_count)