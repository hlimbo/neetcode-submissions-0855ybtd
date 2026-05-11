'''
Brute force O(M * N) search would be to try all rows and columns


O(log(M * N)) time would require application of binary search to find the element
* we know that the 1st integer of every row, is bigger than the last integer of previous row
    * can use the middle row, first element as the pivot point
        * if target > matrix[midRow][0]
            * target must be somewhere between the midRow to lastRow
        * if target < matrix[midRow][0]
            * target must be somwhere between the firstRow and midRow - 1

M is the row and N is the column, you could just search the entire column but that would result in O(log(M) * N) solution


Need to compute the new mid row and new mid col IF target != matrix[midRow][0]
    
    * loRow = 0, hiRow = M
    * loCol = 0, hiCol = N
    * midRow = (loRow + hiRow) // 2
    * midCol = (loCol + hiCol) // 2

    while loRow <= hiRow and loCol < hiCol

    Very top of loop, find out if the target matches matrix[midRow][midCol]

    FIND the row that the target might be in
    * for computing mid row, it would be 
        * if target > matrix[midRow][0]
            loRow = midRow
        * if target < matrix[midRow][0]
            hiRow = midRow - 1

        midRow = (loRow + hiRow) // 2

    matrix[midRow][0] < target < matrix[midRow][-1] ==> I'm somewhere in this row so keep midRow the same

    matrix[midRow-1][0] < target < matrix[midRow-1][-1] ==> I'm somewhere in the previous row so keep midRow the same



    FIND the column the target might be in
    matrix[midRow][0] < target < matrix[midRow][-1] ==> I'm somewhere in this row so keep midRow the same
        if target > matrix[midRow][midCol]
            loCol = midCol + 1
        elif target < matrix[midRow][midCol]
            hiCol = midCol


'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        loRow, hiRow = 0, len(matrix)
        loCol, hiCol = 0, len(matrix[0])

        midRow = (loRow + hiRow) // 2
        midCol = 0

        while loRow < hiRow:
            # we found the row the target might be in
            if matrix[midRow][0] <= target <= matrix[midRow][-1]:
                break
            if target > matrix[midRow][midCol]:
                loRow = midRow + 1
            elif target < matrix[midRow][midCol]:
                hiRow = midRow - 1
                
            midRow = (loRow + hiRow) // 2
        
        iterations = 0
        while loCol < hiCol:
            # out of bounds check
            if midRow >= len(matrix) or midCol >= len(matrix[0]):
                break

            if matrix[midRow][midCol] == target:
                return True
            
            if target > matrix[midRow][midCol]:
                loCol = midCol + 1
            elif target < matrix[midRow][midCol]:
                hiCol = midCol - 1
                
            iterations += 1
                
            midCol = (loCol + hiCol) // 2


        if midRow < len(matrix) and midCol < len(matrix[0]) and matrix[midRow][midCol] == target:
            return True
                
        return False
        