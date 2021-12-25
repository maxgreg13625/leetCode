class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ## 40ms/14.2MB
        #if l1 and l2:
        #    if l1.val > l2.val:
        #        l1, l2 = l2, l1
        #    l1.next = self.mergeTwoLists(l1.next, l2)
        #    return l1
        #else:
        #    return l1 or l2
        ## 40ms/14.3MB
        #if l1 is None:
        #    return l2
        #elif l2 is None:
        #    return l1
        #if l1.val <= l2.val:
        #    l1.next = self.mergeTwoLists(l1.next, l2)
        #    return l1
        #else:
        #    l2.next = self.mergeTwoLists(l1, l2.next)
        #    return l2