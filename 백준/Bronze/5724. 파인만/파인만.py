import sys

square_list = [0] * 101

for i in range(1, 100 + 1):
    if i == 1:
        square_list[i] = 1
        continue

    square_list[i] = square_list[i - 1] + (i * i)

while True:
    N = int(sys.stdin.readline())

    if N == 0:
        break

    print(square_list[N])