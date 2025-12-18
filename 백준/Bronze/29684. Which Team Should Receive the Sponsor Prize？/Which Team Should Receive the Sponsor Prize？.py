import sys

def close_to_2023(second):
    return abs(2023 - int(second))

input = sys.stdin.readline

while True:
    N = int(input())

    if N == 0:
        break

    K_sequence = map(close_to_2023, input().split())
    K_list = [(t, i) for i, t in enumerate(K_sequence, 1)]
    K_list.sort(key=lambda x: x[0])
    winning_team = K_list[0][1]

    print(winning_team)