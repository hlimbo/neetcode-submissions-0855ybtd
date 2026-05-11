# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
You know there is a cycle by using 2 pointers
* pointer A starts at the beginning of the Linked List
* pointer B starts 1 step ahead of the Linked List

* pointer A advances by 1 step
* pointer B advances by 2 steps

* A cycle exists if pointer A points to the same memory address as pointer B
* A cycle does not exist if pointer B reaches a null node which marks end of linked list


'''

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        pointerA = head
        pointerB = head.next

        while pointerB is not None:
            if pointerA == pointerB:
                return True

            pointerA = pointerA.next
            pointerB = pointerB.next.next if pointerB.next is not None else pointerB.next

        return False