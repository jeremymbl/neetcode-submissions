# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not(head):
            return 
        res = ListNode(head.val)
        curr = head.next
        while curr:
            res = ListNode(curr.val, res)
            curr = curr.next
        return res
        