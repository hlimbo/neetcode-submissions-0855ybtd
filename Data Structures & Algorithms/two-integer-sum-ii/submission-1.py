
'''
Knowns
- array is (1-indexed) this means index starts at 1 instead of 0
- sorted in non-decreasing order
    does that mean we can have examples like
        [1,1,3,4,6,7,7,8] ?
- can't use the same index twice
- There will ALWAYS BE EXACTLY ONE VALID SOLUTION

Output
- [index1, index2] where nums[index1] + nums[index2] == target

Constraints
- Must be in O(1) constant space

[1,1,3,4,6,7,7,8]

numbers = [1,2,3,4], target = 3
                     target = 7

[1,1,3,4,6,7,7,8] target = 2
                  target = 10  


Brainstorming
Logic might be
* we place 2 pointers l and r on opposite sides of the array
    if nums[l] + nums[r] < target
        * move l to the left by 1 (can only do that as long as l is in bounds of array)
    if nums[l] + nums[r] > target
        * move r to the right by 1 (can only do that as long as r is in bounds of array)
    if nums[l] + nums[r] == target
        return [l+1,r+1] ... we add 1 because problem tells us to start the index at 1 rather than 0

Other way might be to start the 2 pointers next to each other
* ensure that each pointer is at most 2 spaces away
    - check by doing r - l < 2, then can move r to the right by 1; otherwise move l by 1

O(N) time complexity


'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                # found the combo
                break
        
        return [l+1, r+1]
        