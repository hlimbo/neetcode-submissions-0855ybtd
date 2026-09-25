'''
Inputs:
    * s1 and s2 strings

* Output
    * return true if s2 contains a permutation of s1; false otherwise

* A permutation is a set of characters that all match but are organized in a different order
-- for example --
* abc and cab are permutations
* abc and abx are not permutations

* if len(s1) <= len(s2) --> there could be a permutation s1 that exists as a substring as s2


Questions:
* so for the above to be true, the characters in s2 as a substring need to be next to each other to be considered as a permutation of s1???
* are the characters in s1 all unique or can there be duplicates? there may be duplicates

edge cases:
* if len(s1) > len(s2) --> return false


Data Structures to possibly use:
* HashMap
    * key = character that exists in s1
    * value = number of times character in s1 repeats itself

* sliding window -- 
    * left pointer -> keeps track of where the permutation starts
        - can be used to restore the counter frequency hashmap back to its original counts if a partial substring is found by incrementing left pointer by 1 up to reaching the right pointer
    * right pointer -> keeps track of where the permutation ends

Idea:
* build a hashmap of character frequencies based on s1 called h1
* for each character in s2, check if character exists in h1

* O(N + M) time
* O(N) space

N = len(s1)
M = len(s2)

'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counterMap = {}
        for c in s1:
            if c not in counterMap:
                counterMap[c] = 0
            counterMap[c] += 1

        left, right = 0, 0
        i = 0
        size = 0
        isFirstPartPermFound = False
        while i < len(s2):
            #print("i is: ", i)
            c = s2[i]
            if c in counterMap and counterMap[c] > 0:
                #print(c, " found with ", counterMap[c])
                if not isFirstPartPermFound:
                    isFirstPartPermFound = True
                    left = i

                right = i + 1
                size = right - left
                counterMap[c] -= 1

                # for c in counterMap:
                #     print(c, " ----> ", counterMap[c])

                if size == len(s1):
                    break
            else:
                # partial permutation found, undo markings
                if isFirstPartPermFound:
                    #print("refreshing.... ", left, " -> ", right)
                    for j in range(left, right):
                        counterMap[s2[j]] += 1
                    # for c in counterMap:
                    #     print(c, " -> ", counterMap[c])

                size = 0
                isFirstPartPermFound = False
                # # could be an extra character not in permutation substring
                if c in counterMap:
                    i = left

            i += 1

        isPermutationFound = True
        for c in counterMap:
            if counterMap[c] > 0:
                #print(c, " -> ", counterMap[c])
                isPermutationFound = False
                # break

        return isPermutationFound

        