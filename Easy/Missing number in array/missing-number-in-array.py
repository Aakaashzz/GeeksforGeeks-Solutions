#User function Template for pyt
class Solution:
    def missingNumber(self, array, n):
        s = len(array) + 1
        expectsum = s * (s + 1) // 2
        actualsum = sum(array)
        missing = expectsum - actualsum
        return missing

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