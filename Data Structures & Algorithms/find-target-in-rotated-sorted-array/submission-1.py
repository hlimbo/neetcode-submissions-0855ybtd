'''
O(N) time complexity solution:
* iterate through each element in nums, if num matches target return the index
num matching target was found. if not found, return -1

Assumptions:
* all elements in nums are unique
* arrays are sorted in ascending order
* Must solve it in O(log N) time -> binary search
* array can be rotated between 1 and n times 
* array length between 1 and 1000

Insights:
* if array is rotated n times, then it goes back to its original sorted order
* the biggest number and the smallest number will be next to each other if 
rotated between 1 to n - 1 times

Unknowns:
* we don't know how many times the input array is rotated


Examples

[1,2,3,4,5,6] <-- can apply standard binary search using low and high indices to calc mid index to find the target
[6,1,2,3,4,5]
[5,6,1,2,3,4]
[4,5,6,1,2,3]
[3,4,5,6,1,2]
[2,3,4,5,6,1]

[2,1]
[5]


For an unrotated sorted array, the low and high indices will always be 0 and len(array) - 1

For a rotated sorted array, I'd need to find the pivot index, or the index that has the smallest value first...
* If I can do that then I can locate the max as the max will always be to the left of the minimum where number of rotations is b/w 1 and len(array) - 1


Section A
min_index = (0 + pivot_offset) % len(array)
max_index = (len(array) - 1 + pivot_offset) % len(array)

assumption: 0 <= pivot_offset < len(array)

min_index to standard_min_index conversion
* standard_min_index = min_index - pivot_offset

max_index to standard_max_index conversion
* standard_max_index = max_index - pivot_offset
    if max_index - pivot_offset >= 0
        max_index - pivot_offset
    else
        len(array) - (max_index - pivot_offset)

1. Need to find where pivot_offset lies... --> helper function to find minimum value in rotated sorted array
2. mark min_index and max_index described in Section A
3. use binary search to locate target
    * we will use the standard min and max indices as the condition in the while loop to terminate it
    * left_standard = min_standard_index
    * right_standard = max_standard_index
    * while left_standard < right_standard --> stopping condition

'''


class Solution:
    def findMinValueIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if nums[0] < nums[1]:
                return 0
            else:
                return 1
        
        left, right = 0, len(nums) - 1
        smallest = nums[0]
        smallestIndex = 0
        while left <= right:
            mid = (left + right) // 2

            if smallest > nums[mid]:
                smallest = nums[mid]
                smallestIndex = mid

            # logic to converge both left and right on a shared index
            if nums[left] <= nums[mid] <= nums[right]:
                right = mid - 1
            elif nums[left] >= nums[mid] >= nums[right]:
                left = mid + 1
            elif nums[left] > nums[mid] and nums[right] > nums[mid]:
                if nums[left] > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[left] < nums[mid] and nums[right] < nums[mid]:
                if nums[left] > nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return smallestIndex

    def search(self, nums: List[int], target: int) -> int:
        pivot_offset = self.findMinValueIndex(nums)
        print(f"pivot offset {pivot_offset}")
        # use pivot_offset for figuring out where the target could be located using binary search
        targetIndex = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_offset = (mid + pivot_offset) % len(nums)
            if nums[mid_offset] == target:
                targetIndex = mid_offset
                break

            print(f"nums[{mid_offset}] = {nums[mid_offset]}")

            if nums[mid_offset] > target:
                right = mid - 1
            else:
                left = mid + 1

        return targetIndex