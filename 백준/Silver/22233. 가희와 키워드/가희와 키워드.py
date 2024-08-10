import sys

N, M = map(int, sys.stdin.readline().split())

memo = {sys.stdin.readline().rstrip(): 1 for _ in range(N)}
length = N

for _ in range(M):
    keyword_list = sys.stdin.readline().rstrip().split(',')

    count = 0

    for keyword in keyword_list:
        
        if keyword in memo:
            del memo[keyword]
            count += 1
    
    length -= count

    print(length)