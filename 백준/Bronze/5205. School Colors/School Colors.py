import sys

def calc_distance(a, b):
    r1, g1, b1 = a
    r2, g2, b2 = b

    return (((r2 - r1) ** 2) + ((g2 - g1) ** 2) + ((b2 - b1) ** 2)) ** 0.5

input = sys.stdin.readline

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    RGB_list = [list(map(int, input().split())) for _ in range(N)]

    pair_list = []
    maximum_distance = 0

    for i in range(N):
        A = RGB_list[i]

        for j in range(i + 1, N):
            B = RGB_list[j]
            distance = calc_distance(A, B)

            if distance < maximum_distance:
                continue

            if maximum_distance < distance:
                pair_list.clear()

            pair_list.append((i + 1, j + 1))
            maximum_distance = distance

    print(f'Data Set {t}:')
    
    for pair in pair_list:
        print(*pair)