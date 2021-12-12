class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ##brute force method
        #for i, v1 in enumerate(nums):
        #    for j, v2 in enumerate(nums[i+1:]):
        #        if v1 + v2 == target:
        #            return [i, i+j+1]
        #use python dict as hash table to improve performance
        temp_dict = {}
        for i, v1 in enumerate(nums):
            if target - v1 not in temp_dict:
                temp_dict[v1] = i
            else:
                return [temp_dict[target - v1], i]

assert Solution().twoSum([1, 2, 3, 4, 5, 6], 10) == [3, 5]
assert Solution().twoSum([3, 2, 4], 6) == [1 , 2]
assert Solution().twoSum([3, 3], 6) == [0, 1]