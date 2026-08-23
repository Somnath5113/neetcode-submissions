class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Check Rows
        for row in board:
            nums = [x for x in row if x != "."]
            if len(nums) != len(set(nums)):
                return False
                
        # 2. Check Columns
        for c in range(9):
            col = [board[r][c] for r in range(9) if board[r][c] != "."]
            if len(col) != len(set(col)):
                return False
                
        # 3. Check 3x3 Squares
        for r_start in range(0, 9, 3):
            for c_start in range(0, 9, 3):
                square = []
                # Build the 3x3 square
                for r in range(r_start, r_start + 3):
                    for c in range(c_start, c_start + 3):
                        if board[r][c] != ".":
                            square.append(board[r][c])
                
                if len(square) != len(set(square)):
                    return False
                    
        # If no duplicates were found, the board is valid
        return True