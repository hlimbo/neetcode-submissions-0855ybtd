# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head

        curr = head
        prev = None
        nxt = head.next
        while curr is not None:
            curr.next = prev
            
            if nxt is None:
                break

            prev = curr
            curr = nxt
            nxt = nxt.next

        return curr