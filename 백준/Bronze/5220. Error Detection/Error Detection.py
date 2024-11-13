import sys

T = int(sys.stdin.readline())

for _ in range(T):
    bit, check_bit = map(int, sys.stdin.readline().split())

    bit_sum = sum(map(int, list(bin(bit)[2:])))

    check_number = 0 if bit_sum % 2 == 0 else 1

    if check_number == check_bit:
        print('Valid')
    else:
        print('Corrupt')