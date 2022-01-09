class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # dict and list 4516ms/13.8MB
        result_str = s[0]
        char_loc_dict = {}
        max_length = 1

        for idx, val in enumerate(s):
            pre_list = char_loc_dict.get(val, [])
            if len(pre_list) == 0:
                char_loc_dict[val] = pre_list
            else:
                for pre in pre_list:
                    sub_str = s[pre:idx+1]
                    if sub_str == sub_str[::-1] and\
                        idx - pre + 1 > max_length:
                        max_length = idx - pre + 1
                        result_str = sub_str
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