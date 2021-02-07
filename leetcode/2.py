# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        headThree = None
        count = 0
        while l1 or l2:
            l3_temp = ListNode()
            if headThree is None:
                headThree = l3_temp
                l3 = l3_temp
            else:
                l3.next = l3_temp
                l3 = l3.next
            if l1 and l2:
                l3.val = (l1.val + l2.val + count) % 10
                if l1.val + l2.val + count >= 10:
                    count = 1
                else:
                    count = 0
                l1 = l1.next
                l2 = l2.next
            elif l1:
                l3.val = (l1.val + count) % 10
                if l1.val + count >= 10:
                    count = 1
                else:
                    count = 0
                l1 = l1.next
            elif l2:
                l3.val = (l2.val + count) % 10
                if l2.val + count >= 10:
                    count = 1
                else:
                    count = 0
                l2 = l2.next
        if count == 1:
            l3_temp = ListNode()
            l3.next = l3_temp
            l3_temp.val = 1
        return headThree
