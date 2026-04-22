class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # key = character
        # number of times it occurs in string s
        freqDict = {}

        # logic for if s and t are anagrams of each other
        # they aren't anagrams if there exists a character in t that isn't in s
        # they aren't anagrams if one of the key characters in freqDict has a value != 0

        # build dictionary
        for ch in s:
            if ch not in freqDict:
                freqDict[ch] = 0
        
            freqDict[ch] += 1

        # reduce char count by 1 if there exists a character in t that also is in s
        for ch in t:
            if ch not in freqDict:
                return False
            freqDict[ch] -= 1

            if freqDict[ch] < 0:
                return False

        totalSum = 0
        for ch in freqDict:
            totalSum += freqDict[ch]
        
        return totalSum == 0
