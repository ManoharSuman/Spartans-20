class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        sum1 = 0
        x = A[0]
        for i in A:
            sum1 = sum1+i
            x = max(sum1,x)
            if sum1 < 0:
                sum1 = 0
        return x
