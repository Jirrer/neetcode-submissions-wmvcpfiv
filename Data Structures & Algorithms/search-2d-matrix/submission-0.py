class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lowRow = 0
        highRow = len(matrix) - 1
        while lowRow <= highRow:
            mid = (lowRow + highRow) // 2

            l = 0
            h = len(matrix[mid]) - 1

            while (l <= h):
                m = (l + h) // 2
                val = matrix[mid][m]

                if val == target: return True
                elif val > target: h = m - 1
                else: l = m + 1

            if target < matrix[mid][0]: highRow = mid - 1
            else: lowRow = mid + 1
    
        return False