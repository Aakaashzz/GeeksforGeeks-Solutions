#User function Template for python3

# User function Template for python3

class Solution:
    # Function to find sum of all possible substrings of the given string.
    def sumSubstrings(self, s):
        n = len(s)
        # lookup = [0]*n
        prev = int(s[0])
        mod=10**9+7
        ans=prev
        for i in range(1, n):
            temp=(int(s[i])*(i+1)+10*prev)%mod
            ans=(ans+temp)%mod
            prev=temp
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

import sys
sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s = str(input())
        ob=Solution()
        print(ob.sumSubstrings(s))
# } Driver Code Ends