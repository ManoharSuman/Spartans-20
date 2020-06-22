class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        s = [str(i) for i in A]
        n = int(''.join(s)) + 1
        finallst = [int(i) for i in str(n)]
        return (finallst)
    #
    #     x=A[0]
    #     Final_A=[]
    #     if len(A)==1:
    #         n=(x+1)
    #         print (n)
    #     else:
    #         for i in range(1,len(A)):
    #             x=str(x)+str(A[i])
    #         y=str(int(x)+1)
    #         for i in y:
    #             Final_A.append(i)
    #         print(*Final_A)

