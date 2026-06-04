'''
Input:
* array of nums

Output:
* array of nums where each output is a product

Constraint
* each output[i] is the product of all elements in the array except for nums[i]


Example

input
[3, 2, 8, 1]

output
[2 * 8 * 1, 3 * 8 * 1, 3 * 2 * 1, 3 * 2 * 8]

in this example:
* 8 and 1 repeat in the first half
* 3 and 2 repeat in the second half

One way to do this is for each product to compute
* multiply all the other numbers in the array except for nums[i]
and append it to the end of your output

* This is an O(N^2) time complexity

Goal: O(N) time complexity
what if I get the product of the entire array then initialize it to that
for each one....
After that, to exclude the number you don't want, you would divide by that number to achieve O(N) time

[48, 48, 48, 48]

Goal 2: O(N) time complexity without using division operation....

I know that multiplication is commutative property and associative property

commutative
A * B = B * A

associative
A(BC) = (AB)C 

[3, 2, 8, 1]

left 2 right
[3, 6, 48, 48]

right 2 left
[48, 16, 8, 1]


Example 2
[1, 2, 4, 6]

left 2 right
[1, 2, 8, 48]

right 2 left
[48, 48, 24, 6]

l2r
[1, 1, 2, 8]

r2l
[48, 24, 6, 1]

to get the products of array except self, you create 2 prefix products
l2r where you exclude the current index in the product computation
and r2l where you do the same

then you multiply each corresponding value in each array to get the product except self

O(N) time
O(N) space

Example 3
[3, 2, 8, 1, 9, 4, 7]

[
    2 * 8 * 1 * 9 * 4 * 7, 
    3 * 8 * 1 * 9 * 4 * 7, 
    3 * 2 * 1 * 9 * 4 * 7, 
.......................................
    3 * 2 * 8 * 1 * 4 * 7
    3 * 2 * 8 * 1 * 9 * 7
    3 * 2 * 8 * 1 * 9 * 4
]

'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l2r = []
        r2l = []

        i, j = 0, len(nums) - 1
        while i < len(nums) and j >= 0:
            if i == 0:
                l2r.append(1)
            else:
                l2r.append(l2r[-1] * nums[i-1])
            
            if j == len(nums) - 1:
                r2l.append(1)
            else:
                r2l.append(r2l[-1] * nums[j+1])

            i += 1
            j -= 1
        
        r2l.reverse()
        ans = []
        for i in range(len(l2r)):
            ans.append(l2r[i] * r2l[i])

        return ans