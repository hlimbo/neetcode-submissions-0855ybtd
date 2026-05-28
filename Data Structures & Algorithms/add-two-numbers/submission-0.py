# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
321 is read as 1->2->3 in linked list

321
654

reversed its

123
456
---
579

answer: 975

carrying (this one creates a new node at the end and carries a number throughout)

123
988
---

0121

ans: 1210

since we we add 2 digits (the possible range of it can only be 0 to 9 so any value in the tens place gets carried over to the next set of nodes)

to get the remaining value in the event we do a carry, you do intermediate_sum = l1.val + l2.val
* remaining_digit = intermediate_sum % 10
* carry_digit = intermediate_sum / 10

pseudo-code
* keep track of pointer called c1 for l1
* keep track of pointer called c2 for l2

carry_digit = 0
remaining_digit = 0

create ghost node that will store the sum of what is being returned (sum node)


* as long as c1 and c2 are not null
    intermediate_sum = c1.val + c2.val + carry_digit
    remaining_digit = intermediate_sum % 10
    carry_digit = intermediate_sum // 10

    - create new node and store remaining_digit as its value
    - attach new node to end of sum node
    - adv its pointer to point to the new node just created
    - adv c1 pointer and c2 pointer
    - reset carry_digit to 0

* as long as c1 is not null
    intermediate_sum = c1.val + carry_digit
    remaining_digit = intermediate_sum % 10
    carry_digit = intermediate_sum // 10

    - create new node and store remaining_digit as its value
    - attach new node to end of sum node
    - adv its pointer to point to the new node created
    - adv c1 pointer
    - reset carry_digit to 0

* as long as c2 is not null
    intermediate_sum = c2.val + carry_digit
    remaining_digit = intermediate_sum % 10
    carry_digit = intermediate_sum // 10

    - create new node and store remaining_digit as its value
    - attach new node to end of sum node
    - adv its pointer to point to the new node created
    - adv c2 pointer
    - reset carry_digit to 0

* if carry_digit > 0
    - create a new node storing its value
    - attach new node to end of sum node

set sum to ghost->next
delete ghost

return sum

'''


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_digit = 0
        remaining_digit = 0

        ghost = ListNode(-1)
        c1, c2 = l1, l2
        c3 = ghost

        while c1 and c2:
            intermediate_sum = c1.val + c2.val + carry_digit
            carry_digit = intermediate_sum // 10
            remaining_digit = intermediate_sum % 10

            c3.next = ListNode(remaining_digit)

            c1 = c1.next
            c2 = c2.next
            c3 = c3.next

        
        while c1:
            intermediate_sum = c1.val + carry_digit
            carry_digit = intermediate_sum // 10
            remaining_digit = intermediate_sum % 10

            c3.next = ListNode(remaining_digit)

            c1 = c1.next
            c3 = c3.next

        while c2:
            intermediate_sum = c2.val + carry_digit
            carry_digit = intermediate_sum // 10
            remaining_digit = intermediate_sum % 10

            c3.next = ListNode(remaining_digit)

            c2 = c2.next
            c3 = c3.next

        # number of digits exceed the original length of l1 and l2
        if carry_digit > 0:
            c3.next = ListNode(carry_digit)

        my_sum = ghost.next
        del ghost

        return my_sum
        