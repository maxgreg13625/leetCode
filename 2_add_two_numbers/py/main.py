# Definition for singly-linked list.
from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ## 86ms/13.6MB
        #head_result = temp_result = ListNode()
        #while l1 or l2:
        #    if l1:
        #        temp_result.val = temp_result.val + l1.val
        #        l1 = l1.next
        #    if l2:
        #        temp_result.val = temp_result.val + l2.val
        #        l2 = l2.next
        #    if l1 or l2 or temp_result.val >= 10:
        #        temp_result.next = ListNode()
        #        if temp_result.val >= 10:
        #            temp_result.next.val += 1
        #            temp_result.val = temp_result.val % 10
        #        temp_result = temp_result.next
        #return head_result
        ## 77ms/13.6MB
        #head_result = temp_result = ListNode()
        #while l1 or l2:
        #    if l1 and l2:
        #        temp_result.val = temp_result.val + l1.val + l2.val
        #        l1, l2 = l1.next, l2.next
        #    elif l1:
        #        temp_result.val = temp_result.val + l1.val
        #        l1 = l1.next
        #    else:
        #        temp_result.val = temp_result.val + l2.val
        #        l2 = l2.next
        #    if l1 or l2 or temp_result.val >= 10:
        #        temp_result.next = ListNode()
        #        if temp_result.val >= 10:
        #            temp_result.next.val += 1
        #            temp_result.val = temp_result.val % 10
        #        temp_result = temp_result.next
        #return head_result
        # 52ms/13.5MB
        head_result = temp_result = ListNode()
        while l1 or l2:
            if l1 and l2:
                temp_result.val = temp_result.val + l1.val + l2.val
                l1, l2 = l1.next, l2.next
            elif l1:
                temp_result.val = temp_result.val + l1.val
                l1 = l1.next
            else:
                temp_result.val = temp_result.val + l2.val
                l2 = l2.next
            if l1 or l2 or temp_result.val >= 10:
                temp_result.next = ListNode()
                temp_result.next.val, temp_result.val = divmod(temp_result.val, 10)
                temp_result = temp_result.next
        return head_result