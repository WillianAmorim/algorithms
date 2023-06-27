def find_duplicate(nums):
    if not nums or len(nums) <= 1:
        return False
    nums.sort()

    for i, num in enumerate(nums):
        if isinstance(num, str) or num < 0:
            return False
        if i > 0 and num == nums[i - 1]:
            return num
    return False
