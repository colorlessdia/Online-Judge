number_count = [0] * 10
total = 1

for i in range(3):
    total *= int(input())

for j in str(total):
    number_count[int(j)] += 1

for number in number_count:
    print(number)