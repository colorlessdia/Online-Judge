N = input()

number_count = [0] * 10

for number in N:
    number_count[int(number)] += 1

count_not_6_9 = max(number_count[:6] + number_count[7:9])

duplicate = number_count[6] + number_count[9]
count_6_9 = duplicate // 2 if duplicate % 2 == 0 else (duplicate // 2) + 1

count = max(count_not_6_9, count_6_9)

print(count)