import sys

T = int(sys.stdin.readline())

for _ in range(T):
    number = sys.stdin.readline().rstrip()

    count = 0

    while number != '6174':
        max_number = int(''.join(sorted(number, reverse=True)))
        min_number = int(''.join(sorted(number)))
        
        number = str(max_number - min_number).zfill(4)

        count += 1

    print(count)