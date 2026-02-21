import sys

input = sys.stdin.readline

while True:
    N = int(input())

    if N == 0:
        break

    A = 0

    for i in range(int(N ** 0.5), 0, -1):

        if N % i == 0:
            A = i
            break
    
    B = N // A
    C = 2 * (A + B)

    print(f'Minimum perimeter is {C} with dimensions {A} x {B}')