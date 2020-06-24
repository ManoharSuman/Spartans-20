class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        lenA = len(A)
        temp = [0]*lenA
        for i in A:
            if temp[i - 1]:
                return i
            else:
                temp[i - 1] = 1
        return -1