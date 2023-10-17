def solution(num_list):
    nums = [i for i, num in enumerate(num_list) if num < 0]
    
    return -1 if len(nums) == 0 else nums[0]