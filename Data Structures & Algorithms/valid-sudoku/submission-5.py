class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            real_line = [x for x in board[i] if x != "."]
            if len(real_line) != len(set(real_line)):
                return False
        
        for j in range(9):
            seen = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])
        
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                seen = set()
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if board[k][l] == ".":
                            continue
                        if board[k][l] in seen:
                            return False
                        else:
                            seen.add(board[k][l])

        return True

                
                
        