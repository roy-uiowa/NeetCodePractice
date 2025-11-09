class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        set_rows = set()
        set_cols = set()
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    set_rows.add(i)
                    set_cols.add(j)
        row = [0]*cols
        for i in set_rows:
            matrix[i] = row
        for j in set_cols:
            for r in range(rows):
                matrix[r][j] = 0
        
