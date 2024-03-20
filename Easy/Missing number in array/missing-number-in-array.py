#User function Template for pyt
class Solution:
    def missingNumber(self, array, n):
        a =len(array)+1
        b = a*(a+1)//2
        c = sum(array)
        d = b-c
        return d
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)
# } Driver Code Ends