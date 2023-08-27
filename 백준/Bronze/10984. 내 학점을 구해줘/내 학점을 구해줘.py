import sys

for _ in range(int(input())):
    n = int(input())
    c_total = 0
    g_total = 0

    for _ in range(n):
        c, g = map(float, sys.stdin.readline().split())

        c_total += c
        g_total += c * g

    gpa = g_total / c_total
    print(int(c_total), f'{gpa:.1f}')