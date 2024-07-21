N = int(input())

start = 1
end = 1
sum_value = 1
count = 0

while start <= end:

    if sum_value == N:
        count += 1
        end += 1
        sum_value += end
        continue

    if sum_value < N:
        end += 1
        sum_value += end
        continue
    
    if N < sum_value:
        sum_value -= start
        start += 1
        continue
    
print(count)