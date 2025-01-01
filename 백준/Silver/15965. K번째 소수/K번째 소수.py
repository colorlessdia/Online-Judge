K = int(input())

maximum_number = 10 ** 7

number_list = [0, 0] + ([1] * (maximum_number - 1))

for i in range(2, int(maximum_number ** 0.5) + 1):
    
    if number_list[i] == 0:
        continue

    for j in range(i * 2, maximum_number + 1, i):
        
        if number_list[j] != 0:
            number_list[j] = 0

prime_list = [0] + [k for k in range(maximum_number + 1) if number_list[k]]

print(prime_list[K])