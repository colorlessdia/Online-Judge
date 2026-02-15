import sys

def calc_digit_sum(n):
    return sum([int(char) for char in str(n)])

input = sys.stdin.readline

while True:
    N = int(input())

    if N == 0:
        break

    P = 11
    S = calc_digit_sum(N)

    while True:
        Q = calc_digit_sum(P * N)

        if S == Q:
            print(P)
            break

        P += 1