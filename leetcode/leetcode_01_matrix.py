class Solution:

    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        neighbors = lambda x, y: ((x+1, y), (x-1, y), (x, y+1), (x, y-1))
        is_valid = lambda x, y: 0 <= x < len(mat) and 0 <= y < len(mat[0])

        ret_matrix = [[0 for _ in mat[0]] for _ in mat]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    ret_matrix[i][j] = 0
                else:
                    mini = float('-inf')
                    for x, y in neighbors(i, j):
                        if is_valid(x,y):
                            mini = max(mini, mat[x][y])

                    ret_matrix[i][j] = mini + 1

        return ret_matrix





