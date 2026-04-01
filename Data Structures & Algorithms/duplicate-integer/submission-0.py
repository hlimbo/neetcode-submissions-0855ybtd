class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lookupTable = {}
        for num in nums:
            if num not in lookupTable:
                lookupTable[num] = 0
            lookupTable[num] += 1
            if lookupTable[num] > 1:
                return True
        
        return False