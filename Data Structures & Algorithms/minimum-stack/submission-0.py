'''

for getMin()
* if you push a value into empty array
    * then minimum value is first value
* if you push a value <= than top value, then place it on top of stack
* if you push a value >= than top value, then place it on a 2nd stack
    --> use a 2nd stack to take advantage of the fact that when you pop elements off it and put it onto another stack its order gets reversed

Goal: guarantee 1st stack is ordered in descending order from top to bottom while keeping the 2nd stack strictly greater than the 1st stack

3
2
1
-------

5
10
4

PROBLEM with my current approach is in the push operation where if i pick which stack to push
a value from, I wouldn't know which one to pop from necessarily (in the order i put in this data container)
    -- use a hash map maybe?
        -- key = insert order
        -- value = item i insert

push operation
    * push to 1st stack if its empty
    * if value pushed <= min value, place it on top of 1st stack
    * if value pushed > min value, place it on top of 2nd stack

    insertOrderTable[count] = value to insert
    count += 1

pop operation
    retVal = insertOrderTable[count-1]

    if len(stack1) > 0 and stack1[-1] == retVal:
        stack1.pop()
    elif len(stack2) > 0 and stack2[-1] == retVal:
        stack2.pop()

    count -= 1

    return retVal

top operation
    * peek at the top of 1st stack if 2nd stack empty
    * otherwise peek at the top of 2nd stack

getMin operation
    * peek at the top of the 1st stack

'''


class MinStack:

    def __init__(self):
        self.count = 0
        self.minStack = []
        self.overflowStack = []
        # key - insert order
        # value - element inserted into stack
        self.insertOrderTable = {}

    def push(self, val: int) -> None:
        if len(self.minStack) == 0:
            self.minStack.append(val)
        elif self.minStack[-1] < val:
            self.overflowStack.append(val)
        elif self.minStack[-1] >= val:
            self.minStack.append(val)

        self.insertOrderTable[self.count] = val
        self.count += 1

    def pop(self) -> None:
        valToPop = self.insertOrderTable[self.count - 1]
        del self.insertOrderTable[self.count - 1]
        self.count -= 1
        if len(self.minStack) > 0 and valToPop == self.minStack[-1]:
            self.minStack.pop()
        elif len(self.overflowStack) > 0 and valToPop == self.overflowStack[-1]:
            self.overflowStack.pop()

    def top(self) -> int:
        assert len(self.insertOrderTable) > 0
        return self.insertOrderTable[self.count - 1]

    def getMin(self) -> int:
        assert len(self.insertOrderTable) > 0 and len(self.minStack) > 0
        return self.minStack[-1]

        
