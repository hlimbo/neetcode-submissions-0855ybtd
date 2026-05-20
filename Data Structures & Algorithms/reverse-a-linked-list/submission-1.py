# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
input
0 -> 1 -> 2 -> 3

output
3 -> 2 -> 1 -> 0

----------------------------

# save original pointer to the node it was pointing towards
tmp = c.next
c.next = p
p = c
c = tmp

N  0 -> 1 -> 2 -> 3 -> N
p  c    n

N <- 0 <- 1 <- 2 <- 3     N
                   p     c     n
'''


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev