import sys

def time_to_second(time):
    hh, mm = map(int, time.split(':'))

    return (hh * 60) + mm

def second_to_time(sec):
    hh = str(sec // 60).zfill(2)
    mm = str(sec % 60).zfill(2)

    return f'{hh}:{mm}'

input = sys.stdin.readline

D = 24 * 60

while True:
    s1, s2 = map(time_to_second, input().rstrip().split())
    s3 = s1 + s2

    if s3 == 0:
        break

    P = s3 // D
    Q = s3 % D

    time = second_to_time(Q)

    print(f'{time}{f' +{P}' if P else ''}')