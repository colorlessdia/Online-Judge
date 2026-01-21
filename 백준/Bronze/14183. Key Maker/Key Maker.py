import sys

input = sys.stdin.readline

while True:
    M, N = map(int, input().split())

    if M == N == 0:
        break

    A = list(map(int, input().split()))

    count = 0

    for _ in range(N):
        B = list(map(int, input().split()))

        is_valid = True

        for a, b in zip(A, B):

            if (a - b) < 0:
                is_valid = False

        if is_valid:
            count += 1
    
    print(count)