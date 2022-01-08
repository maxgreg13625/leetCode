class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # use dict to record char previous index  71ms/13.9MB
        if len(s) < 2:
            return len(s)

        char_loc_dict = {}
        max_length, temp_length, start_idx = 0, 0, 0
        for idx, val in enumerate(s):
            pre_loc = char_loc_dict.get(val, -1)

            # update location when not exist before or appear before start index
            if pre_loc == -1 or start_idx > pre_loc:
                char_loc_dict[val] = idx
                temp_length += 1
            else:
                max_length = max(max_length, temp_length)
                # recalculate temp length from next prev idnex
                temp_length = idx - char_loc_dict[val]
                char_loc_dict[val], start_idx = idx, char_loc_dict[val] + 1
        max_length = max(max_length, temp_length)
        return max_length
        # moving window    4656ms/15.6MB
        #length = len(s)
        #if length <= 1:
        #    return length
        #result = 0
        #temp_length = 0
        #for i in range(length-1):
        #    temp_length = 1
        #    for j in range(i+1 , length):
        #        if s[j] in s[i:j]:
        #            break
        #        else:
        #            temp_length += 1
        #    if temp_length > result:
        #        result = temp_length
        #return result

assert Solution().lengthOfLongestSubstring('abcabcbb') == 3
assert Solution().lengthOfLongestSubstring('bbbb') == 1
assert Solution().lengthOfLongestSubstring('pwwkew') == 3
assert Solution().lengthOfLongestSubstring(' ') == 1
assert Solution().lengthOfLongestSubstring('ab') == 2
assert Solution().lengthOfLongestSubstring('aab') == 2
assert Solution().lengthOfLongestSubstring('cdd') == 2
assert Solution().lengthOfLongestSubstring('abba') == 2
assert Solution().lengthOfLongestSubstring('dvdf') == 3