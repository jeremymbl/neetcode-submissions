class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = set()
        boxes = set()

        for i in range(9):
            for j in range(9):
                v = board[i][j]

                if v == ".":
                    continue

                row_key = (i, v)
                col_key = (j, v)
                box_key = (i // 3, j // 3, v)

                if row_key in rows or col_key in cols or box_key in boxes:
                    return False

                rows.add(row_key)
                cols.add(col_key)
                boxes.add(box_key)

        return True