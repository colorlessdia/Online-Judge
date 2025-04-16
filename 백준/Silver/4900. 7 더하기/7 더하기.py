import sys

input = sys.stdin.readline

binary_list = [
    '0111111',
    '0001010',
    '1011101',
    '1001111',
    '1101010',
    '1100111',
    '1110111',
    '0001011',
    '1111111',
    '1101011'
]
code_list = [str(int(binary, 2)).rjust(3, '0') for binary in binary_list]

code_to_number = dict(zip(code_list, map(str, range(9 + 1))))
number_to_code = dict(zip(map(str, range(9 + 1)), code_list))

while 1:
    line = input().rstrip()

    if line == 'BYE':
        break
    
    A, B = line[:-1].split('+')

    a = int(''.join([code_to_number[A[i:i + 3]] for i in range(0, len(A), 3)]))
    b = int(''.join([code_to_number[B[i:i + 3]] for i in range(0, len(B), 3)]))
    c = a + b

    C = ''.join([number_to_code[number] for number in str(c)])

    print(f'{A}+{B}={C}')