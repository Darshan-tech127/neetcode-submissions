class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = defaultdict(set)
        c = defaultdict(set)
        s = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in r[i] or board[i][j] in c[j] or board[i][j] in s[i//3,j//3]:
                    return False
                num = board[i][j]
                r[i].add(num)
                c[j].add(num)
                s[i//3,j//3].add(num)
        return True
                


                


            

                