#User function Template for python3

class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        #code here
        vis = [[0 for j in range(M)] for i in range(N)]
        q = [(0,0,0)]
        delrow = [-1,0,1,0]
        delcol = [0,1,0,-1]
        vis[0][0] = 1
        if X==0 and Y==0:
            if A[0][0] == 1:
                return 0
        while q:
            r,c,dis = q.pop(0)
            for row,col in zip(delrow,delcol):
                nrow = r+row
                ncol = c+col
                if 0<=nrow<N and 0<=ncol<M and not vis[nrow][ncol] and A[nrow][ncol]==1:
                    if nrow==X and ncol==Y:
                        return dis+1
                    vis[nrow][ncol] = 1
                    q.append((nrow,ncol,dis+1))
        return -1


#{ 
 # Driver Code Starts

#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,input().strip().split()))
            a.append(s)
        x,y=map(int,input().strip().split())    
        ob=Solution()
        print(ob.shortestDistance(N,M,a,x,y))
        
# } Driver Code Ends