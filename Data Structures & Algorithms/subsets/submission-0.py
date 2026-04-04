'''
    Choices
    1. include the number
    2. skip the number

Approaches:
1 recursion?
    - state?
        - list of lists = []
        - current subset = []
        - index = 0
    - base case:
        - at end of list --> stop

    choices
        1. include number: 
            subset.append(nums[index])
            recursion(nums, subsets, subset, index + 1)

        -- backtracking --
            subsets.append(subset)
            subset.pop()
        
        2. skip number
            recursion(nums, subsets, subset, index + 1)
            subsets.append(subset)


'''

class Solution:
    def helper(self, nums: List[int], subsets: List[List[int]], subset: List[int], index: int):
        if index >= len(nums):
            subsets.append([num for num in subset])
            return
        
        # include number
        subset.append(nums[index])
        self.helper(nums, subsets, subset, index + 1)

        # backtrack
        subset.pop()

        # skip number
        self.helper(nums, subsets, subset, index + 1)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsetsList = []
        subset = []
        index = 0
        self.helper(nums, subsetsList, subset, index)
        return subsetsList
        