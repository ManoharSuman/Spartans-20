class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints (self, A, B):
        Final_ans = 0
        for i in range(len(A)-1):
            Final_ans = Final_ans+max(abs(A[i]-A[i+1]),abs(B[i]-B[i+1]));
        return Final_ans