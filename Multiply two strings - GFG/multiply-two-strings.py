#User function Template for python3

class Solution:
    def multiplyStrings(self,s1,s2):
        for i in range(0,len(s1)):
            if(s1[i]!=0):
                break
            else:
                s1.replace(s1[i],'')
        for i in range(0,len(s1)):
            if(s2[i]!=0):
                break
            else:
                s2.replace(s2[i],'')
        
        return int(s1)*int(s2)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        a,b=input().split()
        print(Solution().multiplyStrings( a.strip() , b.strip() ))

# } Driver Code Ends