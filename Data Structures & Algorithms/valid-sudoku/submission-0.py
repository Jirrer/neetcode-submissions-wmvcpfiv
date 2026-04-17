class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == ".":
                    continue

                square_index = (r // 3) * 3 + (c // 3)

                if val in rows[r] or val in cols[c] or val in squares[square_index]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                squares[square_index].add(val)

        return True
        
        
        # columns = [[]]
        # rows = []
        # squares = []

        # columnIndex = 0
        # rowIndex = 0

        # while columnIndex < len(board):
        #     if rowIndex == len(board): 
        #         rowIndex = 0
        #         columnIndex += 1
        #         continue

        #     rows.append(board[rowIndex])
        #     if len(columns[-1]) == len(board):
        #         columns.append([])

        #     columns[-1].append(board[rowIndex][columnIndex])
        #     rowIndex += 1

        #     print((rowIndex / 3) * 3 + (columnIndex / 3))
        
        # rowSeen = set()
        # columnSeen = set()

        # for index in range(len(board) - 1):
        #     seen = set()
        #     for x in rows[index]:
        #         if x in seen: return False
        #         else: seen.add(x)

        #     seen = set()
        #     for y in coluns[index]:
        #         if y in seen: return False
        #         else: seen.add(y)

        
        return False