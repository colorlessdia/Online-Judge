import sys

for _ in range(int(input())):
    h, w = map(int, sys.stdin.readline().split())

    bmi = w / ((h / 100) * (h / 100))

    if 204 <= h:
        print(4)
    elif 161 <= h < 204:
        if 20 <= bmi < 25:
            print(1)
        elif 18.5 <= bmi < 20 or 25 <= bmi < 30:
            print(2)
        elif 16 <= bmi < 18.5 or 30 <= bmi < 35:
            print(3)
        elif bmi < 16 or 35 <= bmi:
            print(4)
    elif 159 <= h < 161:
        if 16 <= bmi < 35:
            print(3)
        elif bmi < 16 or 35 <= bmi:
            print(4)
    elif 146 <= h < 159:
        print(4)
    elif 140.1 <= h < 146:
        print(5)
    elif h < 140.1:
        print(6)