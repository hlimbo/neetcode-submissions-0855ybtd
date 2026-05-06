"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

- random pointer points to any node in the list or null

Task: create a deep copy of the list

Output return the head of the copied list


Pretending the random pointer doesn't exists
* to create a copy of the nodes,
    * instantiate a new Node for each node in the original linked list
    * copy the value from original node into new node
    * set next pointer to point to next deeply copied node
    * do this until we reached the end of the original linked list

Issue with this approach is that we don't know if random will point back to a node that we previously visited
from the original or will it point ahead (its random)
* this is an issue because I don't want to inadvertently instantiate more than 1 deep copy of the same node

create a deep copy of each node from the original but don't attach any next or random pointers for them
as those deep copy of those nodes haven't been created yet

brute force way of determining which random is getting pointed for the original list
    - just go through the original list from beginning and see if the reference to random matches that current node reference
    - if you go through all possible nodes and don't find it, random is set to null for that deep copy

[3, 7, 4, 5]

3 -> 7 -> 4 -> 5

"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        # key = node from original list
        # value = node from deep copy list
        originalNodeToCopy = {}
        while curr is not None:
            deepCopy = Node(curr.val)
            originalNodeToCopy[curr] = deepCopy
            curr = curr.next

        # ghost node
        deepCopyRoot = Node(-1)
        curr = head
        curr2 = deepCopyRoot

        while curr:
            deepCopy = originalNodeToCopy[curr]
            curr2.next = deepCopy

            # assign random pointer for deep copy
            if curr.random is not None and curr.random in originalNodeToCopy:
                curr2.next.random = originalNodeToCopy[curr.random]

            curr = curr.next
            curr2 = curr2.next

        temp = deepCopyRoot
        deepCopyRoot = deepCopyRoot.next
        del temp

        return deepCopyRoot
        