N = int(input())
M = int(input())
number_list = sorted(map(int, input().split()))

left = 0
right = len(number_list) - 1

count = 0

while left < right:
    sum_number = number_list[left] + number_list[right]

    if sum_number == M:
        left += 1
        right -= 1
        count += 1
    elif sum_number < M:
        left += 1
    elif M < sum_number:
        right -= 1

print(count)