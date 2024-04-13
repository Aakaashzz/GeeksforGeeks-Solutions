#User function Template for python3
class Solution:
    def reversedBits(self, x):
        # code here 
        sum = 0
        for i in range(32):
            bit = x>>i
            if bit&1:
                sum += 2**(31-i)
            
        return sum 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends