"""
2023.05.15
"""
"""
79. Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        movs = [[1, 0], [0, -1], [0, 1], [-1, 0]]

        def within_board(idx):
            if idx[0] >= 0 and idx[0] < m and idx[1] >= 0 and idx[1] < n:
                return True
            return False

        def helper(w_idx, idx, cache):
            if w_idx == len(word):
                return True
            for mov in movs:
                new_idx = [idx[0] + mov[0], idx[1] + mov[1]]
                if within_board(new_idx) and cache[new_idx[0]][new_idx[1]] and board[new_idx[0]][new_idx[1]] == word[
                    w_idx]:
                    cache[new_idx[0]][new_idx[1]] = False
                    if helper(w_idx + 1, new_idx, cache): # THIS LINE IS CRUCIAL
                        return True # We propagate valid path from recursive calls
                    cache[new_idx[0]][new_idx[1]] = True
            return False

        for i in range(m):
            for j in range(n):
                cache = [[True for _ in range(n)] for _ in range(m)]
                if board[i][j] == word[0]:
                    cache[i][j] = False
                    if helper(1, [i, j], cache):
                        return True
        return False