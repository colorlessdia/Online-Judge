import sys

input = sys.stdin.readline

N = int(input())
A = int(input())

sum_A = 0

for _ in range(N):
    D = int(input())

    if A == D:
        continue

    difference = abs(A - D)
    sum_A += min(difference, 360 - difference)
    
    A = D

print(sum_A)