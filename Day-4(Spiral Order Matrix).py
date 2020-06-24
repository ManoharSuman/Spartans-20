class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        row1 = 0
        col1 = 0
        row2 = A
        col2 = A
        result = [ [0 for i in range(A)] for j in range(A)]
        num = 1
        while num<=A**2:
            for i in range(col1,col2):
                result[row1][i] = num
                num+=1
            if num > A**2:
                break
            for i in range(row1+1,row2):
                result[i][col2-1] = num
                num+=1
            if num > A**2:
                break
            for i in range(col2-2,col1-1,-1):
                result[row2-1][i] = num
                num+=1
            if num > A**2:
                break
            for i in range(row2-2,row1,-1):
                result[i][col1] = num
                num+=1
                row1+=1
                row2-=1
                col1+=1
                col2-=1
        return result
    # Got TLE


