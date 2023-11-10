import sys

for _ in range(int(input())):
    a, b = map(float, sys.stdin.readline().split())
    
    area = (a * 2) / b
    
    print(f'The height of the triangle is {area:.2f} units')