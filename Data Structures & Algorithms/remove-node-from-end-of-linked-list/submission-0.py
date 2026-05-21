# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
questions:
* can n be >= len(list) ? yes
* can n be 0 ? no


O(N) time complexity
O(1) space

how do you know how many nodes are in the list?
* write 1 loop to count for the size


cases (removing)
1. remove node from beginning
- take head node and store it in a tmp variable
- update head node to be the next node in the list
- delete tmp

2. remove node from middle
- check if counter == size - n
    - tmp = curr.next
    - curr.next = curr.next.next
    - delete tmp

3. remove node from end
- walk through the entire list
- once you get curr.next.next == null
    - tmp = curr.next
    - curr.next = curr.next.next
    - delete tmp
'''

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        
        size = 0
        curr = head
        while curr:
            curr = curr.next
            size += 1

        # create a ghost node
        ghost = ListNode(-1, head)
        curr = ghost
        counter = 0
        while curr:
            if counter == size - n:
                tmp = curr.next
                if curr.next:
                    curr.next = curr.next.next
                else:
                    curr.next = None

                del tmp
                break
            
            curr = curr.next
            counter += 1

        head = ghost.next
        del ghost

        return head