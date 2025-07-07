import sys

input = sys.stdin.readline

N = int(input())

coordinates = [0] * N

for i in range(N):
    x, y = map(int, input().split())

    coordinates[i] = (x, y)

sum1 = 0
sum2 = 0

for j in range(N):
    
    if j < N - 1:
        sum1 += coordinates[j][0] * coordinates[j + 1][1]
        sum2 += coordinates[j][1] * coordinates[j + 1][0]
        continue
    
    sum1 += coordinates[j][0] * coordinates[0][1]
    sum2 += coordinates[j][1] * coordinates[0][0]

print(f'{(abs(sum1 - sum2) / 2):.1f}')