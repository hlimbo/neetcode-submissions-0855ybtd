'''
My immediate solution to this problem is to use a set to store the numbers as we walk through the list
- if a duplicate number appears again in the list, return that as the answer
O(N) time and O(N) space due to using a set


To do it in O(1) extra space, you take the value you see in the list and iterate through every OTHER number in the list
* if the same number pops up again in the list, return that value, otherwise keep going until you hit the end of the list
* O(N^2) time complexity....

I know that:
* input array value ranges between 1 and n where n+1 is size of array
*   len(nums) - 1 == POSSIBLE max value of number in array


 0  1  2  3  4
[1, 2, 3, 2, 2]

-1  -2  -3  -1

is it if nums[abs(nums[i]) - 1] == nums[i] ?

questions:
- is the input array sorted? no
- will the max value in the array always be in the input? no
- 

'''


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                return abs(nums[i])
            # mark as visited by negating the value (this might go ahead of what we saw...)
            nums[abs(nums[i]) - 1] *= -1

        # something went wrong here if the input array contains all unique values
        return -1