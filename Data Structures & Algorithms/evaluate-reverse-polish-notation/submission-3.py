'''
Questions:
1. what happens if we encounter a division by zero in the calculation?
2. Will I always receive input that has a valid RPN ?
    * for me a valid RPN means that you get 2 numbers followed by an operator
            "7" "8" "*" ==> 56


Input:
* list of str tokens containing digits as strings and +, -, * or / operators as strings

Output:
* answer represented as an int

Examples
* [5] => 5
* [5, 4] => 5
* [8, 7, *] => 56


- can use stack to keep track of which numbers are stored.. will store up to 2 numbers
where number on bottom of stack is the first value and the top of stack is the second value
[1, 2, -] becomes 1 - 2 = -1 
'''


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            if token == "+":
                b = stk.pop()
                a = stk.pop()
                subAns = a + b
                #print(f"{a} + {b} = {subAns}")
                stk.append(subAns)
            elif token == "-":
                b = stk.pop()
                a = stk.pop()
                subAns = a - b
                #print(f"{a} - {b} = {subAns}")
                stk.append(subAns)
            elif token == "*":
                b = stk.pop()
                a = stk.pop()
                subAns = a * b
                #print(f"{a} * {b} = {subAns}")
                stk.append(subAns)
            elif token == "/":
                b = stk.pop()
                a = stk.pop()
                subAns = int(a / b)
                #print(f"{a} / {b} = {subAns}")
                stk.append(subAns)
            else: # number
                stk.append(int(token))
            
        assert len(stk) <= 2
        return stk[0]