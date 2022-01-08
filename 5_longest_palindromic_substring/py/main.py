class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result_str = ''
        char_loc_dict = {}
        max_length = 0

        for idx, val in enumerate(s):
            pre_list = char_loc_dict.get(val, [])
            if max_length == 0:
                max_length, result_str = 1, val

            if len(pre_list) == 0:
                char_loc_dict[val] = pre_list
            else:
                min_pre, max_pre = min(pre_list), max(pre_list)
                min_sub, max_sub = s[min_pre:idx+1], s[max_pre:idx+1]
                if min_sub == min_sub[::-1] and\
                    idx - min_pre + 1 > max_length:
                    max_length, result_str = idx - min_pre + 1, min_sub
                elif max_sub == max_sub[::-1] and\
                    idx - max_pre + 1 > max_length:
                    max_length, result_str = idx - max_pre + 1, max_sub
            pre_list.append(idx)
        return result_str

assert Solution().longestPalindrome('babad') in ['bab', 'aba']
assert Solution().longestPalindrome('cbbd') in ['bb']
assert Solution().longestPalindrome('bb') in ['bb']
assert Solution().longestPalindrome('a') in ['a']
assert Solution().longestPalindrome('ac') in ['a']
assert Solution().longestPalindrome('abcda') in ['a']
assert Solution().longestPalindrome('aacabdkacaa') in ['aca']
assert Solution().longestPalindrome('babadada') in ['adada']