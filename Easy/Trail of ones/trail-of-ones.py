#User function Template for python3
class Solution:
    def numberOfConsecutiveOnes (ob,n):
        power_of_two = 1
        mod = 1000000007
        dp = [0 ]*(n+1)
        for  i in range(2, n+1):
            dp[i] = (dp[i-1] + power_of_two + dp[i-2]) % mod
            power_of_two =  (power_of_two*2)%mod
        return dp[n] % mod


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        N = int(input())

        ob = Solution()
        print(ob.numberOfConsecutiveOnes(N))

# } Driver Code Ends