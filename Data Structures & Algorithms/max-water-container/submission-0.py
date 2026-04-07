'''
INPUT
* int array heights
    * heights[i] - how tall a bar is

QUESTIONS
* are there bars touching each other or is there some space in between each bar in heights?
    * if there are space between each bar in heights, how much space is in between?
        - assume no space in between the bars to be picked

Task:
* pick 2 bars that trap water in a container WHERE it returns the MAX AMOUNT OF WATER

To obtain the area of water enclosed betweeen any 2 bars:
Area = Width * Height

Height = min(heights[i],heights[j])
Width = j - i where j >= i

Area = (j - i) * min(heights[i], heights[j])

OUTPUT
* int --> area of the max amount of water stored

One way to do it is: O(N^2) time complexity solution
* you try every single possible bar pairing
    * compute bar pair height and width
    * compute the area using bar pair height and width
    * if maxArea < area, then maxArea = area

Another way to do it is by using 2 pointers perhaps?
* I believe the idea behind this problem is you want to find a choice where it maximizes bar height and distance between the bars to obtain max area

O(N) time
- initialize maxArea = 0
- start 2 pointers named l and r at opposite sides of each other in the array
- compute area
- if maxArea < area, then maxArea = area
- move l to the right by 1 if heights[l] < heights[r] otherwise move r to the left by 1

example
    [5, 4, 3, 2, 1]

maxArea = 6

'''


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxValue = 0
        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            area = width * height
            maxValue = max(maxValue, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxValue