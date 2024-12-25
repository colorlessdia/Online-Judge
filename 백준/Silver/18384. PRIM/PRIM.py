import sys
from math import sqrt

maximum_number = 1000000 + 1
number_list = [0, 0] + list(range(2, maximum_number))

for i in range(2, int(sqrt(maximum_number)) + 1):

    for j in range(i * 2, maximum_number, i):
        
        if number_list[j] == 0:
            continue
        
        number_list[j] = 0

T = int(sys.stdin.readline())

for _ in range(T):
    line = list(map(int, sys.stdin.readline().split()))

    total = 0

    for number in line:
        
        for k in range(number, maximum_number):
            
            if number <= number_list[k]:
                total += number_list[k]
                break
    
    print(total)