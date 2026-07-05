# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def aux(acc, lst):
            if lst is None:
                return acc

            return aux(ListNode(lst.val, acc), lst.next)

        return aux(None, head)