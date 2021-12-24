class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # original idea: check the length after no more val in nums  12ms/13.4MB
        while val in nums:
            nums.remove(val)
        return len(nums)


assert Solution().removeElement([3,2,2,3], 3) == 2
assert Solution().removeElement([0,1,2,2,3,0,4,2], 2) == 5