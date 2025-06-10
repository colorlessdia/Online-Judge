import sys

input = sys.stdin.readline

N = int(input())

number_sum = 0
number_list = [0] * N
number_count = dict()

for i in range(N):
    number = int(input())

    number_sum += number
    number_list[i] = number
    number_count[number] = number_count.get(number, 0) + 1

ascending_list = sorted(number_list)
maximum_count = max(number_count.values())
count_list = [k for k, v in number_count.items() if v == maximum_count]
count_list.sort()

arithmetic_mean = int(round(number_sum / N, 0))
median = ascending_list[N // 2]
mode = count_list[0] if len(count_list) == 1 else count_list[1]
number_difference = ascending_list[-1] - ascending_list[0]

print(arithmetic_mean)
print(median)
print(mode)
print(number_difference)