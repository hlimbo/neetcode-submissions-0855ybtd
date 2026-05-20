# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        tail = head
        if head.next:
            tail = self.reverseList(head.next)
            # point the last node back to the current head node of the list
            head.next.next = head

        # head.next is set to none here to prevent infinite linked list cycle
        head.next = None

        return tail