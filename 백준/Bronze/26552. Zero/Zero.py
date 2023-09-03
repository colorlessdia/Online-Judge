import sys

for _ in range(int(input())):
    k = int(sys.stdin.readline())
    
    while 1:
        k += 1
        
        if '0' not in str(k):
            print(k)
            break