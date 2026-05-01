class Solution:
    def isValid(self, s: str) -> bool:
        parensMap = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        parensStack = []
        openParensSet = set()
        openParensSet.add("(")
        openParensSet.add("{")
        openParensSet.add("[")

        for c in s:
            if c in openParensSet:
                parensStack.append(c)
            else:
                if len(parensStack) == 0:
                    return False
                    
                actualOpenParens = parensMap[c]
                expectedOpenParens = parensStack[-1]
                if actualOpenParens != expectedOpenParens:
                    return False
                parensStack.pop()

        print ("len parensStack ", len(parensStack))
        return len(parensStack) == 0
