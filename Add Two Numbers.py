# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d1 = l1
        d2 = l2
        dummy = res = ListNode()
        carry = 0
        while d1 or d2:
            if d1 and d2:
                n = d1.val+d2.val+carry
                d1 = d1.next
                d2 = d2.next
            elif d1: 
                n = d1.val + carry
                d1 = d1.next
            else: 
                n = d2.val + carry
                d2 = d2.next
            if n>=10:
                carry = 1
                n -= 10
            else: carry = 0
            res.next = ListNode(n)
            res = res.next
        if carry: res.next = ListNode(carry)
        return dummy.next

