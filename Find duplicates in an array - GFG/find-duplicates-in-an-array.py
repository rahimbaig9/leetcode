class Solution:
    def duplicates(self, arr, n): 
        temp, res = set(), set()
        
        for i in arr:
            if i not in temp: temp.add(i)
            else: res.add(i)
                
        if res: return sorted(list(res))
        return [-1]
        





#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends