import sys

N = int(sys.stdin.readline())

mine_map = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    row = sys.stdin.readline().rstrip()

    for j in range(N):
        col = row[j]

        if col == '.':
            continue
        
        mine_count = int(col)
        mine_map[i][j] = '*'
        
        k = 0 if i - 1 < 0 else i - 1
        l = N - 1 if N <= i + 1 else i + 1
        m = 0 if j - 1 < 0 else j - 1
        n = N - 1 if N <= j + 1 else j + 1

        for o in range(k, l + 1):
            
            for p in range(m, n + 1):
                area = mine_map[o][p]
                
                if area == '*' or area == 'M':
                    continue
                
                if 10 <= area + mine_count:
                    mine_map[o][p] = 'M'
                else:
                    mine_map[o][p] += mine_count

for map_row in mine_map:
    print(''.join(map(str, map_row)))