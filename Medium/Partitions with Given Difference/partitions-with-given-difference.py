
from typing import List


class Solution:
    def countPartitions(self, n : int, d : int, arr : List[int]) -> int:
        # code here
        s = sum(arr)
        if (s-d)&1 != 0 or s < d:
            return 0

        s = (s-d)//2
 
        dp = [[0]*(n+1) for _ in range(s+1)]
        dp[0][0] = 1
            
        for s0 in range(0, s+1):
            for i in range(1, n+1):
                dp[s0][i] = dp[s0][i-1]
                if s0-arr[i-1] >= 0:
                    dp[s0][i] = (dp[s0][i]+dp[s0-arr[i-1]][i-1])%(10**9+7)

        return dp[s][n]
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        d = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.countPartitions(n, d, arr)
        
        print(res)
        

# } Driver Code Ends