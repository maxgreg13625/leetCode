class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #loop method  56ms/13.7MB
        sx = str(x)
        for idx, val in enumerate(sx):
            if sx[idx] != sx[(idx+1)*-1]:
                return False
        return True
        ##recursive method  66ms/13.5MB
        #x = str(x)
        #if x[0] != x[-1]:
        #   return False
        #elif len(x) <= 2 and x[0] == x[-1]:
        #   return True
        #else:
        #   return self.isPalindrome(x[1:-1])
        ##native python  69ms/13.6MB
        #x = str(x)
        #return x == x[::-1]

assert Solution().isPalindrome(121) == True
assert Solution().isPalindrome(-121) == False
assert Solution().isPalindrome(10) == False
assert Solution().isPalindrome(-101) == False