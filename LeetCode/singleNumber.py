
def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    count = 0
    n = len(nums)
    nums.sort()
    i = 0
    if len(nums) == 1:
        return nums[0]
    while (count < n - 1):
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[i]
        if nums[0] == nums[1]:
            del nums[0]
            del nums[0]
        count += 1

        aaa
