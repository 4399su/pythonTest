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
                if l1.val + l2.val >= 10:
                    l3.val = (l1.val + l2.val) % 10+count
                    count = 1
                else:
                    count = 0
                    l3.val = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                l3.val = l1.val
                l1 = l1.next
            elif l2:
                l3.val = l2.val
                l2 = l2.next

        return headThree
