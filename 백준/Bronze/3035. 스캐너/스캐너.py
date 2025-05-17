import sys

input = sys.stdin.readline

R, C, ZR, ZC = map(int, input().split())

for _ in range(R):
    line = input().rstrip()

    temp = ''

    for char in line:
        temp += char * ZC
    
    for _ in range(ZR):
        print(temp)