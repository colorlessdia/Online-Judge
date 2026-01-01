import sys

input = sys.stdin.readline

N = int(input())

for i in range(1, N + 1):
    M = int(input())

    print(f'Case {i}:')

    for _ in range(M):
        grade = int(input())
        update_grade = grade + 1

        if update_grade < 7:
            print(update_grade)