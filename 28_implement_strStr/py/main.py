class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 12ms/13.9MB
        return haystack.find(needle) if needle in haystack else -1
        ## 16ms/13.7MB
        #return haystack.find(needle)

assert Solution().strStr('hello', 'll') == 2
assert Solution().strStr('aaaa', 'bba') == -1
assert Solution().strStr('', '') == 0