'''
Inputs:
* list of heights
* width of each bar is 1

* Output
* return area of largest rectangle that can be formed among the bars


* One way to solve this is to compute the areas of each bar from the heights input
and store them in an areas array. Then compute the area by expanding the width by 1 each time
but the constraint would be that the height of the new rectangle will be min(heights[i:j])
where i is the starting point and j is the ending point exclusive.

Area = height * width

Area = min(heights[i:j]) * (j - i)
height = min(heights[i:j])
width = (j - i)

This would be approx an O(N^2) time complexity solution as we are trying out all possible rectangles


'''


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        for i in range(len(heights)):
            minHeight = heights[i]

            # get area of single histogram bar
            area = minHeight
            maxArea = max(maxArea, area)

            for j in range(i+1, len(heights)):
                minHeight = min(minHeight, heights[j])
                width = j - i + 1
                area = minHeight * width
                maxArea = max(area, maxArea)

        return maxArea