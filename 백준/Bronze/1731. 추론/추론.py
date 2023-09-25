import sys

nums = [int(sys.stdin.readline()) for _ in range(int(input()))]

if (nums[1] - nums[0]) == (nums[-1] - nums[-2]):
    print(nums[-1] + (nums[1] - nums[0]))
elif (nums[1] // nums[0]) == (nums[-1] // nums[-2]):
    print(nums[-1] * (nums[1] // nums[0]))