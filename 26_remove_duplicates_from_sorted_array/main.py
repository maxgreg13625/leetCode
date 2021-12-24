class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # update the value in original memory address  60ms/14.3MB
        nums[:] = sorted(set(nums))
        return len(nums)
        ##                                             84ms/14.7MB
        #count = 0
        #temp_list = []
        #for n in nums:
        #    if n not in temp_list:
        #        nums[count] = n
        #        count += 1
        #        temp_list.append(n)
        #return len(temp_list)
        # doesn't meet leetcode requirements
        #nums = list(set(nums))
        #return len(nums)

assert Solution().removeDuplicates([1, 1, 2]) == 2
assert Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5