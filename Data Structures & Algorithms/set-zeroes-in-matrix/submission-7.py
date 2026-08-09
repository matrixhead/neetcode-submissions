class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLUMNS = len(matrix[0])

        corner = 1
        for i in range(ROWS):
            for j in range(COLUMNS):
                if matrix[i][j] == 0:
                    if i == 0:
                        corner = 0
                    else:
                        matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,COLUMNS):
            if matrix[0][i] == 0:
                for j in range(ROWS):
                    matrix[j][i] = 0

        for i in range(1,ROWS):
            if matrix[i][0] == 0:
                for j in range(COLUMNS):
                    matrix[i][j] = 0

        if  matrix[0][0] == 0:
            for i in range(ROWS):
                matrix[i][0] = 0

        if corner == 0:
            for i in range(COLUMNS):
                matrix[0][i] = 0
        


        
        