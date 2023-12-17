#User function Template for python3

class Solution:
    def Maximize(self, a, n): 
        
        a.sort()
        return  (sum((x*i) % (10**9 + 7) for i,x in enumerate(a))) % (10**9+7)
        
        
        
        
        
       
        # Complete the function
      



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    print(ob.Maximize(arr, n))
    
# } Driver Code Ends