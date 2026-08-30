class Solution(object):
    def setZeroes(self, matrix):

        r = len(matrix)
        c = len(matrix[0])

        def markinfinity(i, j):
            for x in range(r):
                if matrix[x][j] != 0:
                    matrix[x][j] = float('inf')
            for y in range(c):
                if matrix[i][y] != 0:
                    matrix[i][y] = float('inf')

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    markinfinity(i, j)

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0
