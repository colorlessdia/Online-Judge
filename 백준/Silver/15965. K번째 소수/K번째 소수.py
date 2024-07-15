from math import sqrt

K = int(input())

length = 479909

number_list = [0, 0] + list(range(2, length + 1))

count = 0
prime = 0

for i in range(2, int(sqrt(length + 1)) + 1):
    for j in range(i * 2, length + 1, i):
        number_list[j] = 0

for number in number_list:
    if number != 0:
        count += 1
        prime = number

    if count == K:
        print(prime)
        break