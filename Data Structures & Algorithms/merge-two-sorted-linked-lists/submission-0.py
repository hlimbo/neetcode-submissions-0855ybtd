# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
l1
1 -> 2 -> 4
l2
1 -> 3 -> 5

output
1 -> 1 -> 2 -> 3 -> 4 -> 5

- pointer to l1 named p1
- pointer to l2 named p2


outputRoot node
currOutput ^ pointer that advances depending which p value is smaller

Main logic to determine which pointer to advance
if p1.val < p2.val
    currOutput.next = Node(p1.val)
    advance p1.val
else
    currOutput.next = Node(p2.val)
    advance p2.val

advance currOutput

edge cases
* if p1 and p2 are empty, return null
* if p1 is none or empty, then keep on advancing p2 til its none or empty
* if p2 is none or empty, then keep on advancing p1 til its none or empty

      i
1 2 4
    j
1 3 5

output
1 -> 2 -> 3 -> 4 -> 5
'''

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None

        # ghost node which acts as a placeholder so that we can set the first node from the merge
        outputRoot = ListNode(-1)
        currOutput = outputRoot

        p1, p2 = list1, list2

        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                currOutput.next = ListNode(p1.val)
                p1 = p1.next
            else:
                currOutput.next = ListNode(p2.val)
                p2 = p2.next
            
            currOutput = currOutput.next

        while p1 is not None:
            currOutput.next = ListNode(p1.val)
            currOutput = currOutput.next
            p1 = p1.next

        while p2 is not None:
            currOutput.next = ListNode(p2.val)
            currOutput = currOutput.next
            p2 = p2.next

        temp = outputRoot
        outputRoot = outputRoot.next
        # remove ghost node
        del temp

        return outputRoot