class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list1.extend(list2)
        return sorted(list1)


assert Solution().mergeTwoLists([1, 2, 4], [1, 3, 4]) == [1,1,2,3,4,4]
assert Solution().mergeTwoLists([], []) == []
assert Solution().mergeTwoLists([], [0]) == [0]