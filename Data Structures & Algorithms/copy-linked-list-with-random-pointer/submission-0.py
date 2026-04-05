"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

'''
Questions:
* can I assume the next pointer does not eventually create a cyclic list? i assume no
* can I assume that random might point to its own node or indirectly create a cycle? i assume yes
* can we have an empty list? i assume yes
* can you have nodes that have the same value as other nodes?

Random pointer can:
1. point to nothing --> easy, just set the deep copy's random to null
2. point to itself -->  dictionary to original to random copy
3. point to a different node --> dictionary original to random copy
4. point back to a previous node creating a cycle --> dictionary original to random copy should solve for this

Approach
* create a ghost head node
    [ghost] -> [start of node] -> next item --> so on.... --> null
    - copy each node from the original by iterating through the original using a curr pointer
    - have another curr pointer pointing to the copy

    do a 2nd pass starting from the beginning so that we can assign the random pointers
        - if random pointer points to null, have the copy also point to null (easy)
        - if random pointer points to some node in the original, have copy point to random in the copied list (trickier)
            - tricky because if there are duplicates, how do I know which value the random pointer copy should point to?

hash map implementation 1:
* key = original node 
* value = random pointer copy

hash map 2:
* key: number
* value: list of random pointer copies that all share same key
    [(node copy, index order of original list)]

--> challenge: figuring out if I need to create a new node or not or if its already available?

og 3    -> 7 -> 4 -> 5
cp null    5    3    7

'''


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # key would be the original node
        # value would be deep copy of node
        # we use a hash map here 
        original_to_copy_map = {}

        curr = head
        while curr is not None:
            original_to_copy_map[curr] = Node(curr.val)
            curr = curr.next

        ghost = Node(-101)
        curr_copy = ghost
        curr = head
        while curr is not None:
            node_copy = original_to_copy_map[curr]
            curr_copy.next = node_copy

            if curr.random is None:
                curr_copy.next.random = None
            else:
                curr_copy.next.random = original_to_copy_map[curr.random]

            curr_copy = curr_copy.next
            curr = curr.next

        node_copy_list = ghost.next
        del ghost
        return node_copy_list
        