import sys

for _ in range(int(input())):
    n = list(map(int, sys.stdin.readline().split()))[1:]
    
    index = 1
    
    for i in range(1, len(n)):
        index += 1
        
        if (n[i] - n[i - 1]) != 1:
            print(index)
            break