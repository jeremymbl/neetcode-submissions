class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = set()
        rows = set()
        subs = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (board[i][j], i) in rows:
                    return False
                if (board[i][j], j) in cols:
                    return False
                if (board[i][j], i//3, j//3) in subs:
                    return False
                rows.add((board[i][j], i))
                cols.add((board[i][j], j))
                subs.add((board[i][j], i//3, j//3))
        return True