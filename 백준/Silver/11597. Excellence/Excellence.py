import sys

input = sys.stdin.readline

N = int(input())

score_list = sorted([int(input()) for _ in range(N)])

minimum_score = (10 ** 6) * 2

for i in range(N // 2):
    A = score_list[i]
    B = score_list[-(i + 1)]
    X = A + B

    if X < minimum_score:
        minimum_score = X

print(minimum_score)