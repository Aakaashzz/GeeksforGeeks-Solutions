
from typing import List


class Solution:
    def max_courses(self, n, total, cost):
        dp = [[-1] * (total + 1) for _ in range(n)]
        return self.helper(cost, total, 0, dp)

    def helper(self, arr, total, ind, dp):
        if ind == len(arr):
            return 0
        if dp[ind][total] != -1:
            return dp[ind][total]

        # Don't take the current course
        not_take = self.helper(arr, total, ind + 1, dp)

        # Take the current course if budget allows
        take = 0
        if arr[ind] <= total:
            redeem = int(arr[ind] * 0.9)
            take = 1 + self.helper(arr, total - arr[ind] + redeem, ind + 1, dp)

        # Store the result in the memoization table
        dp[ind][total] = max(not_take, take)
        return dp[ind][total]



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
        
        
        total = int(input())
        
        
        cost=IntArray().Input(n)
        
        obj = Solution()
        res = obj.max_courses(n, total, cost)
        
        print(res)
        

# } Driver Code Ends