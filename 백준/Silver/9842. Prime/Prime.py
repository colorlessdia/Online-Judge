from math import sqrt

n = int(input())

maximun_number = 104729 + 1

number_list = [0, 0] + list(range(2, maximun_number))

for i in range(2, int(sqrt(maximun_number)) + 1):

    for j in range(i * 2, maximun_number, i):
        
        if number_list[j] == 0:
            continue
        
        number_list[j] = 0

prime_list = [0] + [i for i in number_list if i != 0]

print(prime_list[n])