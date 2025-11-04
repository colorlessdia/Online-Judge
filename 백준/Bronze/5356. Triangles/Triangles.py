import sys

input = sys.stdin.readline

T = int(input())

for t in range(1, T + 1):
    N, C = input().rstrip().split()
    N = int(N)

    char_code = ord(C)

    for i in range(1, N + 1):
        print(chr(char_code) * i)
    
        char_code += 1
    
        if ord('Z') < char_code:
            char_code = ord('A')
    
    if t < T:
        print()