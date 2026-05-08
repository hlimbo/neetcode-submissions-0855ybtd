'''
Assumption: it is a 9x9 sudoku board

One Approach:
1. scan row by row
    set rowSet to empty
    for each row
        reset rowSet to empty
        for each col
            if spot is not blank
                if digit is in rowSet
                    return false
                else
                    add digit to rowSet
2. scan col by col
    set colSet to empty
    for each col
        reset colSet to empty
        for each row
            if spot is not blank
                if digit is in colSet
                    return false
                else
                    add digit to colSet
3. scan by 3x3 box
    set boxSet to empty
    for each box index from 0 to 3
        reset boxSet to empty
        for each row from boxIndex * 3 to boxIndex * 3 + 3
            for each col from boxIndex * 3 to boxIndex * 3 + 3
                if spot is not blank
                    if digit is in boxSet
                        return False
                    else
                        add digit to boxSet

If methods 1-3 don't return False early, we can assume that this initial sudoku board state is valid

Logic:
* if a number repeats itself where we can use a set to verify this, then we immediately return
false as we only need to find 1 counter-example that makes this sudoku board state invalid


'''

EMPTY = '.'

class Solution:
    def areRowsValid(self, board: List[List[str]]) -> bool:
        for r in range(len(board)):
            rowSet = set()
            for c in range(len(board[r])):
                if board[r][c] == EMPTY:
                    continue
                digit = board[r][c]
                if digit in rowSet:
                    return False
                else:
                    rowSet.add(digit)

        return True

    def areColsValid(self, board: List[List[str]]) -> bool:
        for c in range(len(board[0])):
            colSet = set()
            for r in range(len(board)):
                if board[r][c] == EMPTY:
                    continue
                digit = board[r][c]
                if digit in colSet:
                    return False
                else:
                    colSet.add(digit)

        return True

    def areBoxesValid(self, board: List[List[str]]) -> bool:
        for br in range(0, 3):
            for bc in range(0, 3):
                boxSet = set()
                for r in range(br * 3, br * 3 + 3):
                    for c in range(bc * 3, bc * 3 + 3):
                        if board[r][c] == EMPTY:
                            continue
                        digit = board[r][c]
                        if digit in boxSet:
                            return False
                        else:
                            boxSet.add(digit)

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.areRowsValid(board) and self.areColsValid(board) and self.areBoxesValid(board)