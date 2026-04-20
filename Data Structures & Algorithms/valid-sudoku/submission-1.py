class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for x in range(len(board))]
        columns = [[] for x in range(len(board))]
        squares = [[] for x in range(len(board))]

        squareIndex = 0 

        for rowIndex in range(len(board)):
            columnIndex = 0
            while columnIndex < len(board):
                rows[rowIndex].append(board[rowIndex][columnIndex])

                columns[rowIndex].append(board[columnIndex][rowIndex])

                squareIndex = (rowIndex // 3) * 3 + (columnIndex // 3)
                print(board[rowIndex][columnIndex], squareIndex)

                if squareIndex < len(squares):
                    squares[squareIndex].append(board[rowIndex][columnIndex])

                columnIndex += 1

        for index in range(len(board)):
            rowSeen = set()
            columnSeen = set()
            squareSeen = set()

            for x in range(len(board)):
                if rows[index][x] in rowSeen: return False
                elif rows[index][x] != '.': rowSeen.add(rows[index][x])

                if columns[index][x] in columnSeen: return False
                elif columns[index][x] != '.': columnSeen.add(columns[index][x])

                if squares[index][x] in squareSeen: return False
                elif squares[index][x] != '.': squareSeen.add(squares[index][x])

        return True