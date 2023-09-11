nums = [int(input()) for _ in range(5)]

for num in nums:
    if nums.count(num) != 2 and nums.count(num) != 4:
        print(num)
        break