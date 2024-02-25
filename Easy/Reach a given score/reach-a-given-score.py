class Solution:
    def count(self, n: int) -> int:
        points = [3, 5, 10]
        dp = [0] * (n + 1)
        dp[0] = 1
    
        for point in points:
            for i in range(point, n + 1):
                dp[i] += dp[i - point]
    
        return dp[n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        ob = Solution()
        print(ob.count(n))
        
# } Driver Code Ends