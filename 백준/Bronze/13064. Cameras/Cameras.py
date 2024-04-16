import sys

n = int(sys.stdin.readline())

for _ in range(n):
    license_plate = sys.stdin.readline().rstrip()

    number_range = '123456789'

    condition1 = all(i in number_range for i in license_plate[:4] + license_plate[5:])
    condition2 = license_plate[0] == license_plate[1]
    condition3 = license_plate[4].isupper()

    if condition1 and condition2 and condition3:
        print(license_plate)