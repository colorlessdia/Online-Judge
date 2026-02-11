import sys

input = sys.stdin.readline

palette = [tuple(map(int, input().split())) for _ in range(16)]

while True:
    R1, G1, B1 = map(int, input().split())

    if R1 == G1 == B1 == -1:
        break

    min_D = float('inf')
    C1, C2, C3 = 0, 0, 0

    for R2, G2, B2 in palette:
        D = ((R2 - R1) ** 2) + ((G2 - G1) ** 2) + ((B2 - B1) ** 2)

        if D < min_D:
            min_D = D
            C1, C2, C3 = R2, G2, B2

    print(f'({R1},{G1},{B1}) maps to ({C1},{C2},{C3})')