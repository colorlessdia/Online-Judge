a, b = map(int, input().split())

sum_list = []
sum_list.append(sum([i for i in range(1, a)]))

for j in range(a, b + 1):
    sum_list.append(sum_list[-1] + j)

total = 1

for k in sum_list[1:]:
    total *= k

print(total % 14579)