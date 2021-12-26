class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 32ms/14.2MB
        length = len(nums)
        if target > nums[-1]:
            return length
        elif target <= nums[0]:
            return 0
        else:
            mid = int(len(nums) / 2)
            if target > nums[:mid][-1]:
                return mid + self.searchInsert(nums[mid:], target)
            else:
                return self.searchInsert(nums[:mid], target)

assert Solution().searchInsert([1, 3, 5, 6], 5) == 2
assert Solution().searchInsert([1, 3, 5, 6], 2) == 1
assert Solution().searchInsert([1, 3, 5, 6], 7) == 4
assert Solution().searchInsert([1], 1) == 0
assert Solution().searchInsert([1, 2, 3, 4, 5, 10], 2) == 1
assert Solution().searchInsert([1, 4, 6, 7, 8, 9], 6) == 2