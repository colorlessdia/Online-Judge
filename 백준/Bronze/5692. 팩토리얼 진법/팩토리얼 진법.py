import sys

def calc_factorial(number):
    factorial = 1
    
    for i in range(number, 0, -1):
        factorial *= i

    return factorial

matched_factorial = [calc_factorial(j) for j in range(1, 5 + 1)]

while True:
    line = sys.stdin.readline().rstrip()[::-1]

    if line == '0':
        break
    
    result = 0
    
    for k in range(len(line)):
        result += matched_factorial[k] * int(line[k])
    
    print(result)