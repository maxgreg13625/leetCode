class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # further simplify                      16ms/13.5MB
        parentheses_dict = {
            '}': '{', ']': '[', ')': '('}
        stack_list = []
        for idx, val in enumerate(s):
            if val not in parentheses_dict:
                stack_list.append(val)
            elif len(stack_list) == 0 or stack_list.pop() != parentheses_dict[val]:
                    return False
        return len(stack_list) == 0
        ## simplify the script logic            16ms/13.7MB
        #parentheses_dict = {
        #    '}': '{', ']': '[', ')': '('}
        #stack_list = []
        #for idx, val in enumerate(s):
        #    if val not in parentheses_dict:
        #        stack_list.append(val)
        #    else:
        #        if len(stack_list) == 0 or stack_list[-1] != parentheses_dict[val]:
        #            return False
        #        else:
        #            stack_list.pop()
        #            continue
        #return len(stack_list) == 0
        ## use dict(hash) and stack to solve   20ms/13.6MB
        #parentheses_dict = {
        #    '}': '{', ']': '[', ')': '('}
        #stack_list = []
        #for idx, val in enumerate(s):
        #    if val not in parentheses_dict:
        #        stack_list.append(val)
        #    else:
        #        if len(stack_list) == 0:
        #            return False
        #        elif len(stack_list) > 0 and stack_list[-1] != parentheses_dict[val]:
        #            return False
        #        else:
        #            stack_list.pop()
        #            continue
        #return True if len(stack_list) == 0 else False
                
assert Solution().isValid('()') == True
assert Solution().isValid('()[]{}') == True
assert Solution().isValid('(]') == False
assert Solution().isValid('(') == False