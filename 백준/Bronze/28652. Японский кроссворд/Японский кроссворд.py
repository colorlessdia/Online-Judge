import sys

def calc_cell(I, J, mode):

    for i in range(I):
        temp = []
        count = 0

        for j in range(J):
            char = ''

            if mode == 'row':
                char = graph[i][j]
            else:
                char = graph[j][i]

            if char == '#':
                count += 1
                continue

            if count:
                temp.append(count)
                count = 0
        
        if count:
            temp.append(count)
            
        print(len(temp), *temp)

input = sys.stdin.readline

R, C = map(int, input().split())

graph = [['.' for _ in range(C)] for _ in range(R)]

for i in range(R):
    row = input().rstrip()

    for j in range(C):
        col = row[j]

        if col == '#':
            graph[i][j] = col

calc_cell(R, C, 'row')
print()
calc_cell(C, R, 'col')