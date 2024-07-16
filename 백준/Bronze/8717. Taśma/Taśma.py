n = int(input())
tape_number = map(int, input().split())

prefix_sum = [0] * (n + 1)

for i, number in enumerate(tape_number, 1):
    prefix_sum[i] = prefix_sum[i - 1] + number

min_difference = None

for j in range(1, n):
    diffrence = abs(prefix_sum[n] - (prefix_sum[j] * 2))
    
    if min_difference == None:
        min_difference = diffrence
        continue

    if diffrence < min_difference:
        min_difference = diffrence

print(min_difference)