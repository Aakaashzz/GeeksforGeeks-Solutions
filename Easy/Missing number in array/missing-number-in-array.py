#User function Template for python3


class Solution:
    def missingNumber(self,array,n):
        array.sort()
        a=1
        for i in range(n-1):
            if array[i]!=a:
                return a
            a+=1
        return a
            
            


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