import sys

def time_to_minute(h, m):
    return (h * 60) + m

def minute_to_time(m):
    return (m // 60, m % 60)

input = sys.stdin.readline

day = time_to_minute(23, 59) + 1

while True:
    H1, M1, H2, M2 = map(int, input().split())

    if H1 == M1 == H2 == H2 == 0:
        break

    t1 = time_to_minute(H1, M1)
    t2 = time_to_minute(H2, M2)

    if t2 < t1:
        t2 += day

    print(t2 - t1)