'''
Knowns
- numbers in list sorted in asc order
- number target
- Must be in O(logn) time

Output
- if target exists, return its index
- otherwise return -1



Examples:
[1, 1, 3, 4, 5, 6] <-- invalid numbers must be unique

[1,3,4,5,6] 
         r
           l
target = 6
target = 1
target = 3
target = 99


Approaches
1. do it recursively where we keep track of a left and right index pointer
2. do it iteratively (no recursion), we use left and right index
    decisions?
        if target == number
            return index
        if target > number
            left = mid + 1
        if target < number
            right = mid - 1
    
        at each iteration, update mid by doing (midpoint formula):
            - mid = (left + right) // 2
    
    0 1 2 3 4 5 6 7 8 9


    we stop checking if left > right

[-1,0,2,4,6,8], target = 4
  l         r
        
'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        mid = (left + right) // 2
        while left <= right:
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            
            mid = (left + right) // 2
        
        return -1
        