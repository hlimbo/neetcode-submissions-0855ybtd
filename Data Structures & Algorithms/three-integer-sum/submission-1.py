'''
Inputs:
* list of nums integer

Outputs:
* List of List of ints
    * represents array of triplets
    * triplet format: [nums[i], nums[j], nums[k]]

Constraints
* nums[i] + nums[j] + nums[k] == 0
* i, j, and k are all distinct

Assumptions:
* can output in any order
* output should not contain duplicate triplets

Questions
* when you mean distinct do you also mean by value like
    [-1, 0, 1] and [0, 1, -1] are not considered distinct?
    ^ not counting permutations by combination triplets? yes

We can do an O(N^3) time complexity solution where we try out all possible permutations....

     i  j  k
[-1, 0, 1, 2, -1, -4]


nums[j] + nums[k] == -nums[i]
  0     +    1    ==   1

  1     +     2  ==    0 no
- store each triplet in its own set so I can do a set comparison in python
to see if they all contain the same set of values between each triplet
- exclude repeated combination this way
([-1, 0, 1],[-1, 1, 2])

-nums[i] == nums[j] + nums[k]

                k
             j                 
          i               
[-4, -1, -1, 0, 1, 2]

'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        tripletSets = set()
        ans = []

        nums.sort()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            target = -1 * nums[i]
            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    potentialTriplet = (nums[i], nums[j], nums[k])
                    isDuplicate = False
                    
                    for triplet in tripletSets:
                        overlappingValues = set(potentialTriplet).intersection(triplet)
                        if len(overlappingValues) == 3:
                            isDuplicate = True
                            break
                    
                    if not isDuplicate:
                        tripletSets.add(potentialTriplet)

                    j += 1

        for triplet in tripletSets:
            ans.append([num for num in triplet])

        return ans