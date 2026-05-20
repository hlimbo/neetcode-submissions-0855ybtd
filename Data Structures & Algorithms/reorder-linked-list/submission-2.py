# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
input
0 1 2 3 4 5 6
s f
  s   f
    s     f
      s        f

0 6 2 3 4 5 1

0 6 1 3 4 5 2

0 6 1 5 4 3 2

0 6 1 5 

output
0 6 1 5 2 4 3

'''


# O(N) time complexity
# O(1) space
# for linked lists problems, I would need a refresher on how to come up with my own algorithms
# for it using either slow, fast pointer method | linked list reversal and pointer manipulation techniques
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle point of list 
        # this works because as you move the fast pointer twice as fast as slow pointer, the slow pointer will stop at the half of the list
        # if not convinced, you can experiment with this code by testing it against an even lengthed and an odd lengthed linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # points to the 2nd half of the original list
        second = slow.next
        # split list into 2 different lists
        slow.next = None
        prev = None
        # reverse 2nd half of the list
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge 2 halfs -- second is the last node
        first, second = head, prev
        while second:
            # store references to next pointers so we don't lose what they originally are
            tmp1, tmp2 = first.next, second.next
            # rewires first.next to point to the 2nd list node that is in reverse order
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
