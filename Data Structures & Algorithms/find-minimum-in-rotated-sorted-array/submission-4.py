'''
Assumptions:
* all elements in rotated array are sorted in ascending order
* all nums in array are unique
* the sorted array may be sorted anywhere between 1 to n times where n is size of array...


Knowns
* if we rotate the element N times, we get the original sorted array
* rotating an array involves shifting all elements to the right by 1
* an element that is the last element in array wraps back around to the 0th index

Task:
* find the min value in the sorted array


What I don't know
* how many times the array was rotated
* where the max value is
* where the min value is

What I do know is that if the rotation isn't a multiple of N, then the smallest and biggest number are right next to each other

O(N) time complexity solution - use the first element as the smallest, look
at each element 1 by 1, if smallest is bigger than current element, current element
becomes the smallest

O(log N) time solution?
* how to apply binary search?
    * we pick the 0th index, last index, and middle index of array
    * left = 0th index
    * right = last index
    * middle = N // 2

    how do I know if we look to the left side or right side of array?
        * [3,4,5,6,1,2] <-- we want to look at the right side of 6 because right index is going in descending order whereas the left index to mid index is ascending order
        * [1,2,3,4,5,6] <-- we want to look at the left side of 4 because left index compared to right index is trending towards descending order
        * [6,1,2,3,4,5] <-- this initial logic of picking the smaller side doesn't work because of the ascending order property
            -- here because the left and right are bigger than mid, we have to check mid's adjacent indices to tell which way to go
            -- we pick left here because 2 < 3 < 4

    -- maybe the key here is to check relative to the midpoint if one side is going in descending order vs ascending order

    Examples

    [1,2,3,4,5,6] y -- nums[left] < nums[mid] < nums[right] -- pick left subarray
    [6,1,2,3,4,5] y -- nums[mid] < nums[left] and nums[mid] < nums[right] (check adjacent mid values -- pick smaller of the 2 to move towards)
    [5,6,1,2,3,4] y -- nums[mid] < nums[left] and nums[mid] < nums[right] (check adjacent mid values -- pick smaller of the 2 to move towards)
    [4,5,6,1,2,3] y -- nums[mid] < nums[left] and nums[mid] < nums[right] (check adjacent mid values -- pick smaller of the 2 to move towards)
    [3,4,5,6,1,2] y -- nums[mid] > nums[left] and nums[mid] > nums[right] pick smallest of nums[left] and nums[right] to move
    [2,3,4,5,6,1] y -- nums[mid] > nums[left] and nums[mid] > nums[right] pick smallest of nums[left] and nums[right] to move
'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        mid = len(nums) // 2
        while left < right:
            if nums[left] <= nums[mid] <= nums[right]: # multiples of N rotations -- ascending order
                right = mid - 1
            elif nums[left] >= nums[mid] >= nums[right]: # descending order
                left = mid + 1
            elif nums[mid] < nums[left] and nums[mid] < nums[right]:
                if nums[mid+1] < nums[mid]:
                    left = mid + 1
                elif nums[mid-1] < nums[mid]:
                    right = mid - 1
                else:
                    break # found smallest
            elif nums[mid] > nums[left] and nums[mid] > nums[right]:
                if nums[left] < nums[right]:
                    right = mid - 1
                elif nums[left] > nums[right]:
                    left = mid + 1
                else:
                    break # found smallest

            if left <= right:
                mid = (left + right) // 2

        return nums[mid]