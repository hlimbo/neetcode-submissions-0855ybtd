# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
For linked lists
- we know that it only goes in 1 direction via the next pointer
- you can't go backwards based on its structure

input
0 1 2 3 4 5 6

The idea here is to do:
1. attach 1st node's next pointer to the last node in the list
2. attach the last node to point to 1st node's original next pointer
* repeat that until you process all nodes in the list....


output
0 6 1 5 2 4 3

p = 6
t = n
n <- 4 <- 5 <- 6

0 1 2 3 | 4 5 6
      s          c 
            

0 1 2 3 | 6 5 4

interleave or alternate nodes from first half and second half

0 6 1 5 2 4 3

Tasks:
* find the middle node of the linked list using the slow and fast pointer method
* reverse 2nd half of the list
* alternate node links between the first half of list and 2nd half of list

'''


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # find middle node of linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        # reverse 2nd half of list
        curr = slow.next
        prev = None
        # remove potential infinite loop by separating the first half of the list from 2nd half of list
        slow.next = None
        while curr:
            # points to original next node in list
            tmp = curr.next
            # have pointer point back to its previous node
            curr.next = prev
            prev = curr
            curr = tmp

        # alternate between first half of list and 2nd half of reversed list
        assert (prev is not None)
        c1 = head
        c2 = prev
        
        #     t     k
        # 0 1 | 3 2
        #   a     b
        # 0 3 1 2 n 

        #       t         k 
        # 0 1 2 3 | 6 5 4
        #     a         b  
        # 0 6 1 5 2 4 3
        while c1 and c2:
            tmp1 = c1.next
            tmp2 = c2.next

            c1.next = c2
            c2.next = tmp1

            c1 = tmp1
            c2 = tmp2