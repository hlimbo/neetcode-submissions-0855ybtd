'''
Assumptions:
* key is considered used if a `get` or `put` operation is called on it

Constraints
* ensure `get` and `put` each run in O(1) average time complexity

Questions:
* when you mean a key is used via get, does that mean if the key doesn't exist when you use `get` will it
create the key in the cache?

LRU - Least Recently Used
* keep track of what was used from most recent to least recent
    * something gets updated to most recent if you put the item in OR you get the item
    * Top of list means item can be removed if a new item is added in when the capacity is reached
    * Bottom of list means item is most recently used
    
    Examples
        * put new item
            * puts key value pair item in cache to bottom of list
            * if at capacity
                * remove item from top of list or least recently used from cache
        * put item (replacement)
            * update existing key value pair item in cache to go to bottom of list
        * get existing item
            * update existing key value pair item in cache to go to bottom of list
        * get non-existing item
            * return -1

Data Structures to use:
* hash map to keep track of which key value pair is stored in cache
    * achieves O(1) average time complexity of accessing the item from get
* which data structure to manage insertion/update order of nodes?
    * array but issue with using array is that you 
    may need to shift elements towards the top of array if cache is at capacity O(N) time complexity
* maybe use a linked list here as it has O(1) removals and O(1) additions
    as long as you know where you start from in the list


Example Dry Run with LRU capacity=2
{1=10, 2=20}

t   b
1 - 2

to add in: {3=30}
--> remove top node
--> end of node (b) gets new attachment 3

t   b
2 - 3

Example Dry Run with LRU capacity=5
{1=10, 2=20, 3=30, 4=40}

add in {5=50}

{1=10, 2=20, 3=30, 4=40, 5=50}

1 - 2 - 3 - 4 - 5

get(2)

1 - 3 - 4 - 5 - 2

{1=10, 3=30, 4=40, 5=50, 2=20}


Doubly Linked List
* head node --> the node that is least recently used
* tail node --> the node that is most recently used

'''

class DLL:
    def __init__(self, key, val, nxt=None, prev=None):
        self.key = key
        self.val = val
        self.next = nxt
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0

        # key = key int
        # val = Doubly Linked List Node ref
        self.lookup = {}
        
        # doubly linked lists
        self.head = None
        self.tail = None
        

    def get(self, key: int) -> int:
        #print(f"getting key {key}")
        if key not in self.lookup:
            return -1

        # update node to be the most recently used
        node = self.lookup[key]
        val = node.val

        # edge case: if node being updated is already most recently used
        if self.tail == node:
            return val

        # edge case: if node being updated is the least recently used, then make sure the new head points 
        # to the next node in the list instead
        if self.head == node and self.size > 1:
            self.head = self.head.next
            self.head.prev = None

        # update connections to exclude current node that may be in middle of list
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        self.tail.next = node
        node.prev = self.tail
        node.next = None
        # update to new tail
        self.tail = self.tail.next

        return val

    def put(self, key: int, value: int) -> None:
        #print(f"putting: {key} -> {value}")
        # update existing key value pair
        if key in self.lookup:
            #print("update existing key")
            node = self.lookup[key]
            node.val = value
            # edge case: node being updated is already the most recently updated
            if self.tail == node:
                return

            # edge case: if node being updated is the least recently used, then make sure the new head points 
            # to the next node in the list instead
            if self.head == node and self.size > 1:
                self.head = self.head.next
                self.head.prev = None

            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev

            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next

            #print(f"tail node key is {self.tail.key}")
            #print(f"head node key is {self.head.key}")
        else:
            #print("add new key")
            # remove LRU node -- head of doubly linked list
            if self.size == self.cap:
                nodeToRemove = self.head
                #print(f"removing node {nodeToRemove.key}")
                
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
                del self.lookup[nodeToRemove.key]
                del nodeToRemove
            else:
                self.size += 1

            # add new key value pair
            node = DLL(key, value)
            self.lookup[key] = node

            if self.head and self.tail:
                self.tail.next = node
                node.prev = self.tail
                node.next = None
                self.tail = self.tail.next
            else:
                if not self.head:
                    self.head = node
                if not self.tail:
                    self.tail = node
  
