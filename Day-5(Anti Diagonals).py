class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        res = [[] for i in range(2 * len(A) - 1)]

        for i in range(len(A)):
            for j in range(len(A)):
                x = i + j
                res[x].append(A[i][j])
        return res