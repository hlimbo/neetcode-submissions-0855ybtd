'''
Task:
* return length of longest substring without duplicate characters -> int

For Sliding Window approach
* you keep track of 2 pointers
    - pointer A and pointer B
    - pointer A is the leftmost boundary of the substring
    - pointer B is the rightmost boundary of the substring

Logic
* expand substring by 1 character by moving pointer B 1 to the right
    as long as the next character is a different character from what was
    already visited... starting from pointer A
* if expand by 1 by using pointer B includes a character already seen
    then move pointer A to the right until the character already seen
    is no longer within the window

The data structure to keep track of which characters are already seen
would be a set because we need to ensure that no repeating characters occur
    within the window

Logic to determine longest substring length
    * use a separate variable called maxLength initialized at 0
    * each time pointer B expands by 1, we compare (pointerB - pointerA) + 1 size to maxLength
        - if maxLength < (pointerB - pointerA) + 1 -> replace maxLength with (pointerB - pointerA) + 1

Time complexity: O(N)
Space: O(N) because we are using a set to store characters from string

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        pointerA, pointerB = 0, 0
        charSet = set()
        
        while pointerB < len(s):            
            # as long as there exists a duplicate character in the set
            # remove all characters starting from left hand side of the window
            # until the duplicate character no longer exists
            while pointerA < pointerB and s[pointerB] in charSet:
                charSet.remove(s[pointerA])
                pointerA += 1

            if s[pointerB] not in charSet:
                charSet.add(s[pointerB])
                currSize = (pointerB - pointerA) + 1
                maxLength = max(maxLength, currSize)
                pointerB += 1

        return maxLength

        