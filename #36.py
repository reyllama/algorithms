"""
2023.03.28
"""
"""
36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""


class Solution:
    def check_duplicate(self, arr):
        from collections import Counter
        c = Counter(arr)
        for i,v in c.items():
            if v > 1:
                if i != ".":
                    return True
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import itertools
        N = len(board) # 9
        for row in board:
            if self.check_duplicate(row):
                return False
        for i in range(N):
            col = [row[i] for row in board]
            if self.check_duplicate(col):
                return False
        for i in range(N):
            r, c = i//3, i%3
            box = list(itertools.chain(*[row[3*c:3*c+3] for row in board[3*r:3*r+3]]))
            if self.check_duplicate(box):
                return False
        return True

"""
Time > 8.52%, Memory > 71.41%
Need to speed up.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cache = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    cur = board[r][c]
                    if (r, cur) in cache or (cur, c) in cache or (r//3, c//3, cur) in cache:
                        return False
                    cache.add((r, cur))
                    cache.add((cur, c))
                    cache.add((r//3, c//3, cur))
        return True
"""
Time > 99.39%, Memory > 71.41%
Traverse each grid point only once, and simultaneously check three conditions.
The difference is in whether to prioritize constraint or position, and in this case the latter is favored.
"""