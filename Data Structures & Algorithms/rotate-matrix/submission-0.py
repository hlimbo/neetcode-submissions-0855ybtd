class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose matrix
        for r in range(len(matrix)):
            for c in range(r, len(matrix[r])):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # reverse each row in the matrix
        for r in range(len(matrix)):
            matrix[r] = matrix[r][::-1]