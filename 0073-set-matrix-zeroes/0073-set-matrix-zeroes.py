class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        first_row = False
        first_col = False
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col = True
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row = True
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1, cols):
                    matrix[i][j] = 0
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(1, rows):
                    matrix[i][j] = 0
        if first_row:
            for j in range(cols):
                matrix[0][j] = 0
        if first_col:
            for i in range(rows):
                matrix[i][0] = 0