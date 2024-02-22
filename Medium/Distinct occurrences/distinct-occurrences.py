class Solution:
    def sequenceCount(self,s, t):
        m=10**9+7
        def calc(ind1,ind2):
            if ind2>=len(t):
                return 1
            if ind1>=len(s):
                return 0
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]%m
            npi=0+calc(ind1+1,ind2)
            pi=0
            if s[ind1]==t[ind2]:
                pi=0+calc(ind1+1,ind2+1)
                
            dp[ind1][ind2]=(pi+npi)%m
            return dp[ind1][ind2]%m
        
        dp=[[-1 for i in range(len(t))] for j in range(len(s))]
        return calc(0,0)


#{ 
 # Driver Code Starts
#Initial template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip().split()
        print(Solution().sequenceCount(str(arr[0]), str(arr[1])))
# } Driver Code Ends