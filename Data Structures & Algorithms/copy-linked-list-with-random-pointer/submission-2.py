"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

'''
Linked List structure
* val -> original value as int value
* next -> pointer to the next node in the list
* random -> a pointer to a new node (could point to the same location as next, could point to null, could point to self, could point anywhere in the linked list)

Task
* create a deep copy of the list

Output:
* return head of copied linked list


Approach
* copy each node from the original by instantiating a new node with the original number
copied over to the copied node
* the copied node would then be put in an array (why? because we don't know if random is
pointing a node that is going to be created in the future and by doing this we can wire the random parameter of the copied node that are copied over)


3 -> 7 -> 4 -> 5 -> null

[3, 7, 4, 5]

From line 32 we can start wiring the head to point to next

To wire the random node copy to copy node, maybe use hash map?
* key = original random node
* value = copied random node

Time complexity: O(N)
* O(N) to create the copies and store in list
* O(N) to build hash map
* O(N) to wire the copied nodes together

Space Complexity: O(N) for storing the nodes in a list and hash map

'''

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copiedNodes = []
        # key - original node reference
        # value - copy node reference
        originalToCopyNodes = {}

        curr = head
        while curr:
            nodeCopy = Node(curr.val)
            originalToCopyNodes[curr] = nodeCopy
            copiedNodes.append(nodeCopy)
            curr = curr.next

        if len(copiedNodes) == 0:
            return None

        # curr = head
        # while curr:
        #     nodeValToRandom[]

        rootCopy = None
        rootCopy = copiedNodes[0]

        curr = head
        randomCopy = originalToCopyNodes[curr.random] if curr.random else None
        rootCopy.random = randomCopy

        currCopy = rootCopy
        curr = curr.next
        for i in range(1, len(copiedNodes)):
            randomCopy = originalToCopyNodes[curr.random] if curr.random else None
            currCopy.next = copiedNodes[i]
            currCopy.next.random = randomCopy
            currCopy = currCopy.next

            curr = curr.next

        return rootCopy
        