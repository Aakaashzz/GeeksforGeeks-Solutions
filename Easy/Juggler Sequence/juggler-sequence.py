#User function Template for python3

from math import *
class Solution:
    def jugglerSequence(self, n):
        ans=[n]
        k=n
        while k!=1:
            if k%2==0:
                s=floor(k**(0.5))
                ans.append(s)
                k=s
            else:
                s=floor(k**(1.5))
                ans.append(s)
                k=s
        return ans
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        arr = ob.jugglerSequence(n)
        for i in (arr):
            print(i, end=" ")
        print()

# } Driver Code Ends