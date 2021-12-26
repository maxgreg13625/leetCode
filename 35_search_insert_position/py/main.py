class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # recursive: 32ms/14.2MB
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
        ## loop solution  36ms/14.3MB
        #i = 0
        #j = len(nums) - 1
        #while(i <= j):
        #    pivot = (i + j) // 2
        #    if (nums[pivot] == target):
        #        return pivot
        #    elif (nums[pivot] >= target):
        #        j = pivot - 1
        #    else:
        #        i = pivot + 1
        #return i

assert Solution().searchInsert([1, 3, 5, 6], 5) == 2
assert Solution().searchInsert([1, 3, 5, 6], 2) == 1
assert Solution().searchInsert([1, 3, 5, 6], 7) == 4
assert Solution().searchInsert([1], 1) == 0
assert Solution().searchInsert([1, 2, 3, 4, 5, 10], 2) == 1
assert Solution().searchInsert([1, 4, 6, 7, 8, 9], 6) == 2