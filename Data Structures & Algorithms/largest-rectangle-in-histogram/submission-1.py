class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        
        stack = []
        leftMost = [-1] * len(heights)
        for i in range(len(heights)):
            while len(stack) > 0 and heights[i] <= heights[stack[-1]]:
                stack.pop()

            if stack:
                leftMost[i] = stack[-1]
            
            stack.append(i)

        stack = []
        rightMost = [len(heights)] * len(heights)
        for i in range(len(heights)-1,-1,-1):
            while len(stack) > 0 and heights[i] <= heights[stack[-1]]:
                stack.pop()

            if stack:
                rightMost[i] = stack[-1]

            stack.append(i)

        print(f"leftmost: {leftMost}")
        print(f"rightmost: {rightMost}")

        maxArea = 0
        for i in range(len(heights)):
            # why do this part? -- this removes the off by 1 error when computing the areas
            leftMost[i] += 1
            rightMost[i] -= 1

            maxArea = max(maxArea, heights[i] * (rightMost[i] - leftMost[i] + 1))

        return maxArea