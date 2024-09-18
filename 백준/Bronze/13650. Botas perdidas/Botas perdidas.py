import sys

while True:
    line = sys.stdin.readline().rstrip()

    if line == '':
        break
    
    boots_count = dict()
    
    N = int(line)

    for _ in range(N):
        M, L = sys.stdin.readline().rstrip().split()

        if M in boots_count:
            
            if L == 'E':
                boots_count[M][0] += 1
            elif L == 'D':
                boots_count[M][1] += 1
        
            continue
        
        if L == 'E':
            boots_count[M] = [1, 0]
        elif L == 'D':
            boots_count[M] = [0, 1]
    
    count = 0

    for left, right in boots_count.values():
        count += min(left, right)
    
    print(count)