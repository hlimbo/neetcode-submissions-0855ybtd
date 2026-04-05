'''
input: list of nums

knowns:
* i != j
* target
* return answer with smaller index first!
    -> do a swap operation here
* only 1 valid answer exists

output: return indices i and j where nums[i] + nums[j] == target

approach
* brute force
    * for each number x
        for each number except x named y
            if x == y: skip
            if x + y == target:
                return [x_index, y_index] --> swap order if x_index > y_index

* use hash map
    * key: the difference between target and nums[j]
    * value: array of indices that contain duplicate nums[i]

    * idea
        * nums[i] = target - nums[j]

    # assume diff is in nums if it isn't then it won't ever be looked up in the other loop
    for each index, num in nums:
        diff = target - num
        if diff not in map:
            map[diff] = []
        
        map[diff].append(index)

    for index, num in nums:
        if num in map:
            indices = map[num]
            for other_index in indices:
                if other_index != index:
                    if index < other_index:
                        return [index, other_index]
                    else:
                        return [other_index, index]


6: [0]
5: [1]
4: [2]

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in lookup:
                lookup[diff] = []
            lookup[diff].append(i)

        for i in range(len(nums)):
            num = nums[i]
            if num in lookup:
                indices = lookup[num]
                for j in indices:
                    if i == j:
                        continue
                    if i < j:
                        return [i , j]
                    else:
                        return [j, i]
        
        # something wrong happened if no answer can be found here
        return [-1, -1]
        