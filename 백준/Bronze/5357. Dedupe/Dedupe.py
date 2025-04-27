import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    line = input().rstrip()

    temp = line[0]

    for char in line[1:]:
        
        if temp[-1] == char:
            continue
        
        temp += char

    print(temp)