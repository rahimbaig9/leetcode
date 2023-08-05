#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):

        A.sort()
        ma=max(A)
        for i in range(0,N-M+1):
            dif=0
            j=i+M-1
            dif=A[j]-A[i]
            if ma>=dif:
                ma=dif
        return ma
            
 
            
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends