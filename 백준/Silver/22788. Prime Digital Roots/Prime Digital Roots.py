import sys
from math import sqrt

maximum_number = 999999 + 1

number_list = [0, 0] + list(range(2, maximum_number))

for i in range(2, int(sqrt(maximum_number)) + 1):
    
    for j in range(i * 2, maximum_number, i):
        
        if number_list[j] != 0:
            number_list[j] = 0

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break
    
    is_prime = number_list[n]

    if is_prime:
        print(f'{str(n).rjust(7)} {str(n).rjust(7)}')
        continue

    number = n

    is_digital_root = False

    while 10 <= number:
        number = sum(map(int, str(number)))

        if number_list[number] != 0:
            is_digital_root = True
            break
    
    digital_root = str(number) if is_digital_root else 'none'

    print(f'{str(n).rjust(7)} {digital_root.rjust(7)}')