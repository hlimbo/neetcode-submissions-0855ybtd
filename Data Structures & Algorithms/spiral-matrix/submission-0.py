'''
1x1
2 -> 2

3x4
1 2 3
4 5 6
7 8 9
1 2 3

1 - 2 - 3 - 6 - 9 - 3 - 2 - 1 - 7 - 4 - 5 - 8

4x4

1 2 3 4
5 6 7 8
9 8 7 6
5 4 3 2

1 - 2 - 3 - 4 - 8 - 6 - 2 - 3 - 4 - 5 - 9 - 5 - 6 - 7 - 7 - 8


4x3
1 2 3 4
5 6 7 8
9 10 11 12

1 2 3 4 8 12 11 10 9 5 6 7


Need offsets for minRow, maxRow AND minCol, maxCol

1. Left to Right
    - when this finishes minRow increases by 1
2. Top to Bottom
    - when this finishes maxCol is reduced by 1
3. Right to Left
    - when this finishes maxRow is reduced by 1
4. Bottom to Top
    - when this finishes minCol increases by 1
5. Repeat until all elements are visited (visitCount == M x N)

'''



class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 1:
            return matrix[0]

        ans = []
        N, M = len(matrix), len(matrix[0])
        minRow, maxRow = 0, N
        minCol, maxCol = 0, M
        dirIndex = 0

        while len(ans) < N * M:

            if dirIndex == 0:
                # left to right
                for c in range(minCol, maxCol):
                    ans.append(matrix[minRow][c])
                
                minRow += 1

            elif dirIndex == 1:
                # top to bottom
                for r in range(minRow, maxRow):
                    ans.append(matrix[r][maxCol-1])

                maxCol -= 1

            elif dirIndex == 2:
                # right to left
                for c in range(maxCol-1, minCol-1, -1):
                    ans.append(matrix[maxRow-1][c])

                maxRow -= 1
            else:
                # bottom to top
                for r in range(maxRow-1, minRow-1, -1):
                    ans.append(matrix[r][minCol])

                minCol += 1

            dirIndex = (dirIndex + 1) % 4

        return ans
        