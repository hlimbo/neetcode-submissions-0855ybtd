'''
Input:
* array of non-negative integers representing height
* each value of height[i] represents bar's height
* each bar has a width of 1

Output:
* return max area of water that can be trapped b/w the bars


Examples:
* if all heights are 0, max area is 0


input:
[0, 2, 0, 3, 1, 0, 1, 3, 2, 1]

output:
9

examples

1,2,3,4,5,6 ==> this holds 0 rain water because you need a high,low, high bar pattern to trap rain water in between
5,4,3,2,1 ==> same thing for this one
2,2,2,2,2 ==> this holds 0 because all the bars at same height

Questions
* do you need at least a width of 3 to trap rain water (including the left and right bars)? yes
* do the bars that are not as tall take up the space that normal rain water would be on? yes
* if you have 2 bars where they are at least 1 space or more away from each other,
then could you have water trapped in there?


I would need to maybe use 2 pointer approach
* l tracks the left hand side of where water gets trapped
* r tracks the right hand side where water gets trapped


to get area of a rectangle where water gets trapped in
* (r - l) * min(height(l, r))
    --> assuming the height for all bars in between are equal
* (r - l) * min(height(l, r)) - sum of bar heights in between l and r

== count the number of bars in between whose height > 1
* these bars will be used to subtract from bar area

     |
  |  |      
_ |  ||  ||

- if bars ascend where bars[i] <= bars[i+1], then i becomes i+1
- bars descend where bars[i] > bars[i+1], then we have a j that goes past i+1
- if j - i > 1 and  bars[i] <= bars[j]
    - record area between these 2 bars

'''


class Solution:    
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res