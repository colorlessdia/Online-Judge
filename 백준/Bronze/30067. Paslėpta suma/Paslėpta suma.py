nums = [int(input()) for _ in range(10)]

for i in range(10):
    if sum(nums[:i] + nums[i + 1:]) == nums[i]:
        print(nums[i])
        break