import sys

input = sys.stdin.readline

N = int(input())

serial_dict = dict()

for _ in range(N):
    serial = input().rstrip()

    length = len(serial)
    sum_number = sum([int(char) for char in serial if char.isnumeric()])

    if length not in serial_dict:
        serial_dict[length] = []
    
    serial_dict[length] += [(sum_number, serial)]

for _, v in sorted(serial_dict.items(), key=lambda x: x[0]):
    sorted_v = sorted(v, key=lambda x: (x[0], x[1]))
    
    for _, sorted_serial in sorted_v:
        print(sorted_serial)