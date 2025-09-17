number_sum = 0
number_count = dict()

for _ in range(10):
    N = int(input())

    number_sum += N

    if N not in number_count:
        number_count[N] = 1
    else:
        number_count[N] += 1

print(number_sum // 10)
print(sorted(number_count.items(), key=lambda x: -x[1])[0][0])